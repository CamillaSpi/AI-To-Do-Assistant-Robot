# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from unicodedata import category

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, ReminderScheduled,SessionStarted,ActionExecuted,EventType,FollowupAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from datetime import datetime, timedelta
from dateutil import parser
import pytz
import hashlib

from . import Database
from time import sleep
import json
import os

global id
id = None

global rasa_only
rasa_only = False

#this script inizialize the conversation with the chatbot.
#append lots of event: sessionStarted, all ReminderScheduled, ActionExecuted and eventually a slotSet for name
#this actions is really important for our applications, also to reload reminders fixed before in last conversations
class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[EventType]:
        global id
        global rasa_only
        # the session should begin with a `session_started` event
        events = [SessionStarted()]
        amdam_tz = pytz.timezone('Europe/Amsterdam')
        actual_time = datetime.now()
        actual_time_tz = amdam_tz.localize(actual_time, is_dst = True)
        global id
        id=tracker.current_state()["sender_id"]
     
        try:
            id = int(id) #if yes this id was send trough ros nose
            Database.initDb(0)       
        except:
            rasa_only = True
            Database.initDb(1)    

        lista = Database.getAllReminder()
        print(len(lista), 'reminder ripristinati')
        for element in lista:
            deadline = element[3]
            time_remind = parser.parse(deadline)-timedelta(seconds = 300)
            if(time_remind < actual_time_tz):
                time = datetime.now()+timedelta(seconds = 2)
                entities = [{'id':element[0],'name':Database.getName(element[0]), 'activity':element[1], 'category':element[2],'deadline': deadline,'expired':True}] # 'time':time
            else: 
                time = time_remind
                entities = [{'id':element[0],'name':Database.getName(element[0]), 'activity':element[1], 'category':element[2],'deadline': deadline,'expired':False}] # 'time':time
            events.append(ReminderScheduled(
                "EXTERNAL_reminder",
                trigger_date_time = time,
                entities = entities,
                kill_on_user_message = False,
            ))
        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))
        if rasa_only==False:
            events.append(SlotSet("name", 'tmp'))

        return events

#this script create an user in the chatcot.
#call a more low level function of database_connectivity.py Database.createUser
#to insert the new user if the operation could not be performed return the name of the already existent ones.
class actionCreateUser(Action):

    def name(self) -> Text:
        return "action_recognize_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = tracker.get_slot("name")

        global id
        id=tracker.current_state()["sender_id"]
        
        try:
            id = int(id)
        except:
            m = hashlib.sha256()
            id = m.update(str(name.lower()).encode())
            
            m.digest()
            id = m.hexdigest()
     
        if(Database.doesUserExists(id) == False):
            returnedValue = Database.createUser(id,name)
            dispatcher.utter_message(text=f"{name} il tuo account è stato correttamente creato!") 
            
        else:
            name = Database.getName(id)
            dispatcher.utter_message(text=f"{name} hai effettuato l'accesso!") 
        return []

#this script perform add activity action.
#call a more low level function of database_connectivity.py Database.insertItem eventually call also actionAddCategory if the category not exist.
#it try to be quite robust to eventually miss understanding of the chatbot, (list of entity etc.)
#if the operation is performed inform ROS through dispatcher.utter_message it is really important for the tablet functionalities
# at the end reset all necessary Slot

class actionAddItem(Action):

    def name(self) -> Text:
        return "action_add_item"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global id
        if not rasa_only:
            id=int(tracker.current_state()["sender_id"])

        associated_name = Database.getName(id)
        if associated_name == None: # if user ask somethings without previously login
            actionCreateUser.run(self,dispatcher,tracker,domain)
            associated_name = Database.getName(id)
        activity = tracker.get_slot("activity")
        category = tracker.get_slot("category")
        reminder = tracker.get_slot("reminder")
        time = tracker.get_slot("time")
        if (isinstance(activity,list)):
            activity = ' '.join([str(elem) for elem in activity])
        if (isinstance(category,list)):
            category = ' '.join([str(elem) for elem in category])
        if(time != None and len(time) == 2):
            time = time['to']
        if(Database.doesPossessionExists(id,category)):
            returnedValue= Database.insertItem(id,activity ,category,reminder,time)
            if (returnedValue):  
                text = f"{associated_name}, l'attività {activity} è stata aggiunta alla categoria {category}" + (f", da completare prima del {time[:10]} alle {time[11:16]}." if time else ".") + ("Te lo ricorderò" if reminder else "") 
                if rasa_only:
                    dispatcher.utter_message(text=text) 
                else:
                    dispatcher.utter_message(text=text,json_message={'query':'js'}) 
            else:
                dispatcher.utter_message(text=f"Ops {associated_name}, questa attività esiste già.") 
        else:
            dispatcher.utter_message(text=f"Questa categoria non esisteva, l'ho creata.") 
            actionAddCategory.run(self, dispatcher,tracker,domain, sender=False)
            actionAddItem.run(self, dispatcher,tracker,domain)
        
        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]


#this script perform remove activity action.
#call a more low level function of database_connectivity.py Database.deleteItem.
#it try to be quite robust to eventually miss understanding of the chatbot, (list of entity etc.)
#if the operation is performed inform ROS through dispatcher.utter_message it is really important for the tablet functionalities
# at the end reset all necessary Slot

class actionRemoveItem(Action):

    def name(self) -> Text:
        return "action_remove_item"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        global id
        if not rasa_only:
            id=int(tracker.current_state()["sender_id"])

        associated_name = Database.getName(id)
        if associated_name == None:
            actionCreateUser.run(self,dispatcher,tracker,domain)
            associated_name = Database.getName(id)
        activity = tracker.get_slot("activity")
        category = tracker.get_slot("category")
        time = tracker.get_slot("time")
        if (isinstance(activity,list)):
            activity = ' '.join([str(elem) for elem in activity])
        if (isinstance(category,list)):
            category = ' '.join([str(elem) for elem in category])
        returnedValue = Database.deleteItem(id,activity ,category,time)
        if (returnedValue):
            text = f"{associated_name}, l'attività {activity} è stata rimossa dalla categoria {category} ."
            if rasa_only:
                dispatcher.utter_message(text=text) 
            else:
                dispatcher.utter_message(text=text,json_message={'query':'js'}) 
        else:
            dispatcher.utter_message(text=f"Mi dispiace {associated_name}, questà attività non esiste.") 


        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

#this script perform add category action.
#call a more low level function of database_connectivity.py Database.insertCategoryAndPossession
#it try to be quite robust to eventually miss understanding of the chatbot, (list of entity etc.)
#if the operation is performed inform ROS through dispatcher.utter_message it is really important for the tablet functionalities
# at the end reset all necessary Slot

class actionAddCategory(Action):

    def name(self) -> Text:
        return "action_add_category"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any], sender=True) -> List[Dict[Text, Any]]: 
        global id
        if not rasa_only:
            id=int(tracker.current_state()["sender_id"])
        
        associated_name = Database.getName(id)
        if associated_name == None:
            actionCreateUser.run(self,dispatcher,tracker,domain)
            associated_name = Database.getName(id)
        print("qunato vale sender:", sender)
        category = tracker.get_slot("category")
        if (isinstance(category,list)):
            category = ' '.join([str(elem) for elem in category])
        returnedValue = Database.insertCategoryAndPossession(id,category)
        if (returnedValue):  
            text = f"{associated_name}, {category} è stata aggiunta come nuova categoria."
            if rasa_only:
                dispatcher.utter_message(text=text) 
            else:
                if sender==True:
                    dispatcher.utter_message(text=text,json_message={'query':'js'}) 
        else:
            dispatcher.utter_message(text=f"{associated_name}, questa categoria esiste già.") 

    
        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

#this script perform remove category action.
#call a more low level function of database_connectivity.py Database.deleteCategory
#it try to be quite robust to eventually miss understanding of the chatbot, (list of entity etc.)
#if the operation is performed inform ROS through dispatcher.utter_message it is really important for the tablet functionalities
# at the end reset all necessary Slot

class actionRemoveCategory(Action):

    def name(self) -> Text:
        return "action_remove_category"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        global id
        if not rasa_only:
            id=int(tracker.current_state()["sender_id"])

        associated_name = Database.getName(id)
        if associated_name == None:
            actionCreateUser.run(self,dispatcher,tracker,domain)
            associated_name = Database.getName(id)
        category = tracker.get_slot("category")
        if (isinstance(category,list)):
            category = ' '.join([str(elem) for elem in category])
        returnedValue = Database.deleteCategory(id,category)
        if (returnedValue):  
            text = f"{associated_name}, la categoria {category} è stata rimossa."
            if rasa_only:
                dispatcher.utter_message(text=text) 
            else:
                dispatcher.utter_message(text=text,json_message={'query':'js_reload'}) 
        else:
            dispatcher.utter_message(text=f"{associated_name}, questa categoria non esiste.") 

        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

#this script perform set complete activity action.
#call a more low level function of database_connectivity.py Database.setItemStatus
#it try to be quite robust to eventually miss understanding of the chatbot, (list of entity etc.)
#if the operation is performed inform ROS through dispatcher.utter_message it is really important for the tablet functionalities
# at the end reset all necessary Slot

class actionSetStatusActivity(Action):

    def name(self) -> Text:
        return "action_set_status_activity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global id
        if not rasa_only:
            id=int(tracker.current_state()["sender_id"])

        associated_name = Database.getName(id)
        if associated_name == None:
            actionCreateUser.run(self,dispatcher,tracker,domain)
            associated_name = Database.getName(id)
        activity = tracker.get_slot("activity")
        category = tracker.get_slot("category")
        activity_status = tracker.get_slot("activity_status")
        time = tracker.get_slot("time")
        if (isinstance(activity,list)):
            activity = ' '.join([str(elem) for elem in activity])
        if (isinstance(category,list)):
            category = ' '.join([str(elem) for elem in category])
        if activity_status == 'completata':
            returnedValue = Database.setItemStatus(id,activity ,category,time,True)
        elif activity_status == 'incompleta':
            returnedValue = Database.setItemStatus(id,activity ,category,time,False)
        else:
            dispatcher.utter_message(text=f"{associated_name}, non ho capito cosa vuoi fare, perfavore ripeti in maniera più chiara.") 
            return [SlotSet("activity", None),SlotSet("category", None),SlotSet("time",None),SlotSet("activity_status",None)]

        if (returnedValue):  
            text = f"{associated_name}, l'attività {activity} in {category} è {activity_status} !"
            if rasa_only:
                dispatcher.utter_message(text=text) 
            else:
                dispatcher.utter_message(text=text,json_message={'query':'js'}) 
        else:
            dispatcher.utter_message(text=f"{associated_name}, questa attività non esiste.") 

        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

#this script perform set uncompleted activity action.
#call a more low level function of database_connectivity.py Database.setItemStatus
#it try to be quite robust to eventually miss understanding of the chatbot, (list of entity etc.)
#if the operation is performed inform ROS through dispatcher.utter_message it is really important for the tablet functionalities
# at the end reset all necessary Slot

class actionSetInComplete(Action):

    def name(self) -> Text:
        return "action_set_uncomplete"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global id
        if not rasa_only:
            id=int(tracker.current_state()["sender_id"])
     
        associated_name = Database.getName(id)
        if associated_name == None:
            actionCreateUser.run(self,dispatcher,tracker,domain)
            associated_name = Database.getName(id)
        activity = tracker.get_slot("activity")
        category = tracker.get_slot("category")
        time = tracker.get_slot("time")
        if (isinstance(activity,list)):
            activity = ' '.join([str(elem) for elem in activity])
        if (isinstance(category,list)):
            category = ' '.join([str(elem) for elem in category])
        returnedValue = Database.setItemStatus(id,activity ,category,time,False)

        if (returnedValue):  
            dispatcher.utter_message(text=f"{associated_name}, l'attività {activity} in {category} impostata come incompleta.") 
        else:
            dispatcher.utter_message(text=f"{associated_name}, questa attività non esiste.") 

        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

#this script perform show activity action.
#call a more low level function of database_connectivity.py Database.selectItems
#it try to be quite robust to eventually miss understanding of the chatbot, (list of entity etc.)
#if the operation is performed inform ROS through dispatcher.utter_message it is really important for the tablet functionalities
# in fact tells the query that is required to be done to show on Pepper tablet the activities (change based on the user request)
# at the end reset all necessary Slot

class showActivities(Action):
    def name(self) -> Text:
        return "action_view_activities"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global id
        if not rasa_only:
            id=int(tracker.current_state()["sender_id"])
        
        associated_name = Database.getName(id)
        if associated_name == None:
            actionCreateUser.run(self,dispatcher,tracker,domain)
            associated_name = Database.getName(id)

        category = tracker.get_slot("category")
        activity_status = tracker.get_slot("activity_status")
        time = tracker.get_slot("time")
        if (isinstance(category,list)):
            category = ' '.join([str(elem) for elem in category])
        list_of_activity,json = Database.selectItems(id,category, activity_status, time)
        text=associated_name
        if json == None:
            text += f", ecco le tue attività:\n\t {list_of_activity}." if list_of_activity else " non ci sono attività per te!"
        else:
            text += f", hai {list_of_activity} attività." if list_of_activity else " non ci sono attività per te!"
        dispatcher.utter_message(text=text,json_message=json) 

        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

#this script perform show Categories action.
#call a more low level function of database_connectivity.py Database.selectPossessions
#if the operation is performed inform ROS through dispatcher.utter_message it is really important for the tablet functionalities
# in fact tells the query that is required to be done to show on Pepper tablet the categories (change based on the user request)
# at the end reset all necessary Slot

class showCategories(Action):
    def name(self) -> Text:
        return "action_view_categories"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global id
        if not rasa_only:
            id=int(tracker.current_state()["sender_id"])
        
        associated_name = Database.getName(id)
        if associated_name == None:
            actionCreateUser.run(self,dispatcher,tracker,domain)
            associated_name = Database.getName(id)
        list_of_categories,json = Database.selectPossessions(id)
        text = associated_name
        if json == None:
            text+=f", ecco le tue categorie: {list_of_categories}." if list_of_categories else " non hai alcuna categoria!"
        else:
            text+=f"(, hai {list_of_categories} categorie." if list_of_categories else " non ci sono categorie per te!"

        
        dispatcher.utter_message(text=text,json_message=json) 

        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

#this script perform modify Categories action.
#call a more low level function of database_connectivity.py Database.modifyCategory
#it try to be quite robust to eventually miss understanding of the chatbot, (list of entity etc.)
#if the operation is performed inform ROS through dispatcher.utter_message it is really important for the tablet functionalities
# at the end reset all necessary Slot

class actionModifyCategory(Action):
    def name(self) -> Text:
        return "action_modify_category"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global id
        if not rasa_only:
            id=int(tracker.current_state()["sender_id"])
        
        associated_name = Database.getName(id)
        if associated_name == None:
            actionCreateUser.run(self,dispatcher,tracker,domain)
            associated_name = Database.getName(id)
        category_old = tracker.get_slot("category_old")
        if (isinstance(category_old,list)):
            category_old = ' '.join([str(elem) for elem in category_old])
        category_new = tracker.get_slot("category_new")
        if (isinstance(category_new,list)):
            category_new = ' '.join([str(elem) for elem in category_new])
        
        if (Database.doesPossessionExists(id,category_new) == False):
            print(category_new)
            returnedValue = Database.modifyCategory(id, category_old, category_new)
            if (returnedValue):  
                text = f"{associated_name}, categoria {category_old} modificata in {category_new} ."
                if rasa_only:
                    dispatcher.utter_message(text=text) 
                else:
                    dispatcher.utter_message(text=text,json_message={'query':'js_reload'}) 
            else:
                dispatcher.utter_message(text=f"{associated_name} , la categoria {category_old} non esiste.") 
        else:
            dispatcher.utter_message(text=f"{associated_name} , la categoria {category_new} esiste già.") 
        
        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

#this script perform modify Activity action.
#call a more low level function of database_connectivity.py Database.modifyActivity
#it try to be quite robust to eventually miss understanding of the chatbot, (list of entity etc.)
#it is quite more complex because the modify for the activities could be very different (modify deadline,modify activity name,modify category name, etc..)
#if the operation is performed inform ROS through dispatcher.utter_message it is really important for the tablet functionalities
# at the end reset all necessary Slot

class actionModifyActivity(Action):
    def name(self) -> Text:
        return "action_modify_activity"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        possibleDeadlineErrorFlag=False
        global id
        if not rasa_only:
            id=int(tracker.current_state()["sender_id"])

        category_old = tracker.get_slot("category_old")
        activity_old = tracker.get_slot("activity_old")
        activity_new = tracker.get_slot("activity_new")
        category_new = tracker.get_slot("category_new")
        category = tracker.get_slot("category")
        activity = tracker.get_slot("activity")
        time = tracker.get_slot("time")
        if (isinstance(activity_old,list)):
            activity_old = ' '.join([str(elem) for elem in activity_old])
        if (isinstance(activity_new,list)):
            activity_new = ' '.join([str(elem) for elem in activity_new])
        if (isinstance(activity,list)):
            activity = ' '.join([str(elem) for elem in activity])
        if (isinstance(category,list)):
            category = ' '.join([str(elem) for elem in category])
        if (isinstance(category_new,list)):
            category_new = ' '.join([str(elem) for elem in category_new])
        if (isinstance(category_old,list)):
            category_old = ' '.join([str(elem) for elem in category_old])
        associated_name = Database.getName(id)
        if associated_name == None:
            actionCreateUser.run(self,dispatcher,tracker,domain)
            associated_name = Database.getName(id)
        
        if(activity_old!=None):
            act_to_modify = activity_old
        else:
            act_to_modify = activity
        if(category_old!=None):
            cat_to_modify = category_old
        else:
            cat_to_modify = category
        
        if(time != None and len(time) == 2 and not isinstance(time, list)):
            if(time['to'] != None):
                tmp = str(datetime.strptime(time['to'], "%Y-%m-%dT%H:%M:%S.%f%z") - timedelta(days=1)).split(" ")
                timenew = tmp[0] + "T" + (tmp[1])[:-6] + ".000" + (tmp[1])[-6:]
                
            else:
                timenew = time['from'] 
            timeold = time['from']
        elif(isinstance(time, list)):
            timeold = time[0]['from']
            timenew = time[1]
        elif(Database.doesUnfoldingsExists(id,category,activity) and category_new == None and activity_new == None):
            
            timenew = time
            timeold = None
        else:
            possibleDeadlineErrorFlag=True
           
            timenew = time
            timeold = time
        if possibleDeadlineErrorFlag is True and activity_old is None and category_old is None:
            dispatcher.utter_message(text=f"Perfavore, ripeti la richiesta specificando la deadline attuale e quella nuova")
            return [SlotSet("category", None),SlotSet("category_old", None),SlotSet("activity_old", None),SlotSet("category_new", None),SlotSet("activity_new", None),SlotSet("activity", None),SlotSet("time", None)]
    

        if(category_new == None):
            category_new = category
        if(activity_new == None):
            activity_new = activity
        
      
        if (Database.doesUnfoldingsExists(id,category_new,activity_new,timenew) == False):
            print("nel db sto per cercare: ", id, cat_to_modify, act_to_modify, timeold,category_new, activity_new, timenew)
            returnedValue = Database.modifyActivity(id, cat_to_modify, act_to_modify, timeold,category_new, activity_new, timenew)
            if (returnedValue):  
                text = f"{associated_name}, l'attività {act_to_modify} è stata modificata"
                if rasa_only:
                    dispatcher.utter_message(text=text) 
                else:
                    dispatcher.utter_message(text=text,json_message={'query':'js'}) 
            else:
                dispatcher.utter_message(text=f"{associated_name} , l'attività da modificare non esiste.") 
                
        else:
            dispatcher.utter_message(text=f"{associated_name} l'attività {activity_new} esiste già, non ha senso modificare {act_to_modify}") 
    
        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

#this script perform set Reminder slot.

class actionSetReminderSlot(Action):
    def name(self) -> Text:
        return "action_set_reminder_slot"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("reminder",True)]

#this script clean completed activities action.
#call a more low level function of database_connectivity.py Database.cleanCompletedActivities(id)
#if the operation is performed inform ROS through dispatcher.utter_message it is really important for the tablet functionalities

class actionCleanCompletedActivities(Action):
    def name(self) -> Text:
        return "action_clean_all_completed"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global id
        if not rasa_only:
            id=int(tracker.current_state()["sender_id"]) 
        
        associated_name = Database.getName(id)
        if associated_name == None:
            actionCreateUser.run(self,dispatcher,tracker,domain)
            associated_name = Database.getName(id)         
        
        returnedValue = Database.cleanCompletedActivities(id)
        if (returnedValue):  
            text = f"{associated_name}, tutte le tue attività completate sono state rimosse!"
            if rasa_only:
                dispatcher.utter_message(text=text) 
            else:
                dispatcher.utter_message(text=text,json_message={'query':'js'}) 
        else:
            dispatcher.utter_message(text=f"{associated_name} qualcosa è andato storto! Non rho potuto rimuovere le tue attività completate!") #??
    
        return []

#this script perform Slots reset.

class actionResetSlot(Action):
    def name(self) -> Text:
        return "action_reset_slot"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        return [SlotSet("activity_old",None),
        SlotSet("activity",None),
        SlotSet("category_old",None),
        SlotSet("category",None),
        SlotSet("time",None),
        SlotSet("activity_status",None)
        ]

#this script perform chatbot reset.
#append lots of event: sessionStarted, FollowupAction("action_session_start"), and a slotSet for name
#this operation same times are necessary, in fact is impossible to create a chatbot that is always in a propositive status,
# if it go in a wrong way with this command return to an operative status

class actionResetConversation(Action):
    def name(self) -> Text:
        return "action_reset_tracker"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not rasa_only:
            return [SessionStarted() ,FollowupAction("action_session_start"),SlotSet("name", 'tmp')]
        else:
            return [SessionStarted() ,FollowupAction("action_session_start"),SlotSet("name", None)]


#this script perform reminder update for activities action.
#it calculate the correct time to be set for the reminder and call a more low level function of database_connectivity.py Database.updateReminder
#it try to be quite robust to eventually miss understanding of the chatbot, (list of entity etc.)
#if the operation is performed inform ROS through dispatcher.utter_message it is really important for the tablet functionalities
# at the end reset all necessary Slot

class actionRemindItem(Action):
    def name(self) -> Text:
        return "action_reminder_item"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global id
        if not rasa_only:
            id=int(tracker.current_state()["sender_id"])

        activity = tracker.get_slot("activity")
        category = tracker.get_slot("category")
        reminderSlot = tracker.get_slot("reminder")
        time = tracker.get_slot("time")
        
        associated_name = Database.getName(id)
        if associated_name == None:
            actionCreateUser.run(self,dispatcher,tracker,domain)
            associated_name = Database.getName(id) 
        date = parser.parse(time) -timedelta(seconds = 300)
        amdam_tz = pytz.timezone('Europe/Amsterdam')
        actual_time = datetime.now()
        actual_time_tz = amdam_tz.localize(actual_time, is_dst = True)

        expired = False

        if(date < actual_time_tz):
            date = datetime.now()+timedelta(seconds = 2)
            expired=True
        if (isinstance(activity,list)):
            activity = ' '.join([str(elem) for elem in activity])
        if (isinstance(category,list)):
            category = ' '.join([str(elem) for elem in category])
        entities = [{'id':id,'name':Database.getName(id), 'activity':activity, 'category':category,'deadline': time,'expired':expired}] # 'time':time
        reminder = ReminderScheduled(
            "EXTERNAL_reminder",
            trigger_date_time = date,
            entities = entities,
            kill_on_user_message = False,
        )

        if (Database.doesUnfoldingsExists(id,category,activity,time)):
            
            returnedValue = Database.updateReminder(id,category,activity,time,reminderSlot)
            if (returnedValue):
                text = f"{associated_name}, il reminder per l'attività è stato aggiornato."
                if rasa_only:
                    dispatcher.utter_message(text=text) 
                else:
                    dispatcher.utter_message(text=text,json_message={'query':'js'}) 
            else:
                dispatcher.utter_message(text=f"{associated_name}, ci sono stati dei problemi con l'aggiornamento del reminder!")
        else:
            actionAddItem.run(self,dispatcher,tracker,domain)
        
        return [SlotSet("activity",None), SlotSet("time",None), SlotSet("category",None),SlotSet("reminder",False),reminder]
        
# this are support script to perform the action of modify the category of an activity,
# in fact set the correct slot from simple category to category old,
# in that way the chatbot will ask for category new performing in a good way this operation
# at the end reset all necessary Slot

class actionAskCategoryOld(Action):
    def name(self) -> Text:
        return "action_ask_category_old"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        category_old = tracker.get_slot("category_old")
        category = tracker.get_slot("category")
        if(category_old == None and category == None):
            dispatcher.utter_message(text=f"Qual è la categoria da modificare?")
            return[SlotSet("requested_slot","category")]
        else:
            dispatcher.utter_message(text=f"Qual è la nuova categoria?")
            return[SlotSet("category_old",category),SlotSet("category",None),SlotSet("category_new",None),SlotSet("requested_slot","category")]    

# this are support script to perform the action of modify the category of an activity,
# in fact set the correct slot from simple category to category new,
# in that way the chatbot will performs in a good way this operation
# at the end reset all necessary Slot

class actionAskCategoryNew(Action):
    def name(self) -> Text:
        return "action_ask_category_new"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        category_new = tracker.get_slot("category_new")
        category = tracker.get_slot("category")
        category_old = tracker.get_slot("category_old")
        if(category_new == None and (category == None or category == category_old)):
            dispatcher.utter_message(text=f"Qual è la nuova categoria?")
            return[SlotSet("requested_slot","category")]
        else:
            return[SlotSet("category_new",category),SlotSet("category",None),SlotSet("requested_slot",None)]    

# this are support script to perform the action of modify the name of an activity,
# in fact set the correct slot from simple activity to activity old,
# in that way the chatbot will ask for activity new performing in a good way this operation
# at the end reset all necessary Slot

class actionAskActivityOld(Action):
    def name(self) -> Text:
        return "action_ask_activity_old"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        activity_old = tracker.get_slot("activity_old")
        activity = tracker.get_slot("activity")
        if(activity_old == None and activity == None):
            dispatcher.utter_message(text=f"Qual è l'attività da modificare?")
            return[SlotSet("requested_slot","activity")]
        else:
            dispatcher.utter_message(text=f"Qual è la nuova attività?")
            return[SlotSet("activity_old",activity),SlotSet("activity",None),SlotSet("activity_new",None),SlotSet("requested_slot","activity")]    

# this are support script to perform the action of modify the name of an activity,
# in fact set the correct slot from simple activity to activity new,
# in that way the chatbot will performs in a good way this operation
# at the end reset all necessary Slot

class actionAskActivityNew(Action):
    def name(self) -> Text:
        return "action_ask_activity_new"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        activity_new = tracker.get_slot("activity_new")
        activity = tracker.get_slot("activity")
        activity_old = tracker.get_slot("activity_old")
        if(activity_new == None and (activity == None or activity == activity_old)):
            dispatcher.utter_message(text=f"Qual è la nuova attività?")
            return[SlotSet("requested_slot","activity")]
        else:
            return[SlotSet("activity_new",activity),SlotSet("activity",None),SlotSet("requested_slot",None)]    
        

class ActionReactToReminder(Action):
    """Reminds the user to call someone."""

    def name(self) -> Text:
        return "action_react_to_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message.get("entities")[0]
        name = entities['name']
        id_user = entities['id']
        deadline = entities['deadline']
        activity = entities['activity']
        category = entities['category']
        expired = entities['expired']
        print(expired)
        Database.updateReminder(id_user,category, activity, deadline, False)
        if(expired):
            text = f"{name}, il reminder per l'attività {activity} in {category} è scaduto!"
            if rasa_only:
                dispatcher.utter_message(text=text) 
            else:
                dispatcher.utter_message(text=text,json_message={'query':'js'}) 
            print("ti sei scordato ", activity, category)
        else: 
            text = f"{name}, ricordati dell'attività {activity} in {category} tra cinque minuti!"
            if rasa_only:
                dispatcher.utter_message(text=text) 
            else:
                dispatcher.utter_message(text=text,json_message={'query':'js'}) 
            print("sei ancora in tempo per ricordarti", activity, category)

        return []

class ActionRecognizeUser(Action):
    """Return the name of the user"""

    def name(self) -> Text:
        return "action_say_name"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        global id
        if not rasa_only:
            id=int(tracker.current_state()["sender_id"])
        
        associated_name = Database.getName(id)
        if associated_name == None:
            actionCreateUser.run(self,dispatcher,tracker,domain)
            associated_name = Database.getName(id) 

        dispatcher.utter_message(f"Hey penso tu sia {associated_name}!")

        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None), SlotSet("name", associated_name)]