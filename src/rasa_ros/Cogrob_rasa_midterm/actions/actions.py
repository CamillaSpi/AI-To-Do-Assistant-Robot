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
from rasa_sdk.events import SlotSet, ReminderScheduled,SessionStarted,ActionExecuted,EventType
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from datetime import datetime, timedelta

from . import Database

class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[EventType]:
        # the session should begin with a `session_started` event
        events = [SessionStarted()]
        # lista = Database.getAllReminder()
        # print(len(lista), 'reminder ripristinati')
        # for element in lista:
        #     time = datetime.now() + timedelta(seconds = 20000) # time = datetime.fromisoformat(element[3])
        #     entities = [{'name':Database.getName(element[0]), 'activity':element[1], 'category':element[2]}] # 'time':time
        #     events.append(ReminderScheduled(
        #         "EXTERNAL_reminder",
        #         trigger_date_time = time,
        #         entities = entities,
        #         kill_on_user_message = False,
        #     ))
        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))

        return events

class actionCreateUser(Action):

    def name(self) -> Text:
        return "action_recognize_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        id=tracker.current_state()["sender_id"]
        id = 5

        if(Database.doesUserExists(id) == False):
            returnedValue = Database.createUser(id,name)

            dispatcher.utter_message(text=f"Congratulation {name} your account has been correctly created") 
            
        else:
            name = Database.getName(id)
            dispatcher.utter_message(text=f"Congratulation {name} you're logged in") 
        return []


class actionAddItem(Action):

    def name(self) -> Text:
        return "action_add_item"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        
        id=tracker.current_state()["sender_id"]

        id = 5
        associated_name = Database.getName(id)
        activity = tracker.get_slot("activity")
        category = tracker.get_slot("category")
        reminder = tracker.get_slot("reminder")
        time = tracker.get_slot("time")
        if(time != None and len(time) == 2):
            time = time['to']

        
        if(Database.doesPossessionExists(id,category)):
            returnedValue= Database.insertItem(id,activity ,category,reminder,time)
            if (returnedValue):  
                text = f"Congratulation {associated_name}, {activity} added to {category}" + (f", complete before {time[:10]} at {time[11:16]}." if time else ".") + (" I will remind you, dont worry " if reminder else "") 
                dispatcher.utter_message(text=text) 
            else:
                dispatcher.utter_message(text=f"Ops {associated_name}, this activity already exists.") 
        else:
            dispatcher.utter_message(text=f"The category does not exists! I'm creating it!") 
            actionAddCategory.run(self, dispatcher,tracker,domain)
            actionAddItem.run(self, dispatcher,tracker,domain)
        
        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

class actionRemoveItem(Action):

    def name(self) -> Text:
        return "action_remove_item"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        name = tracker.get_slot("name")
      
        id=tracker.current_state()["sender_id"]
        associated_name = Database.getName(id)
        activity = tracker.get_slot("activity")
        category = tracker.get_slot("category")
        time = tracker.get_slot("time")

        returnedValue = Database.deleteItem(id,activity ,category,time)
        if (returnedValue):  
            dispatcher.utter_message(text=f"Congratulation {associated_name}, {activity} removed from {category}") 
        else:
            dispatcher.utter_message(text=f"Ops {associated_name}, this activity does not exists.") 


        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]
    

class actionAddCategory(Action):

    def name(self) -> Text:
        return "action_add_category"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        name = tracker.get_slot("name")
        
        id=tracker.current_state()["sender_id"]
        id = 5
        associated_name = Database.getName(id)
        category = tracker.get_slot("category")

        returnedValue = Database.insertCategoryAndPossession(id,category)
        if (returnedValue):  
            dispatcher.utter_message(text=f"Congratulation {associated_name}, {category} added as a new category") 
        else:
            dispatcher.utter_message(text=f"Ops {associated_name}, this category already exists.") 

    
        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]
    

class actionRemoveCategory(Action):

    def name(self) -> Text:
        return "action_remove_category"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        
        name = tracker.get_slot("name")
        id=tracker.current_state()["sender_id"]
        
        associated_name = Database.getName(id)
        category = tracker.get_slot("category")

    
        returnedValue = Database.deleteCategory(id,category)
        if (returnedValue):  
            dispatcher.utter_message(text=f"Congratulation {associated_name}, category {category} removed") 
        else:
            dispatcher.utter_message(text=f"Ops {associated_name}, this  category does not exists.") 


        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

class actionSetStatusActivity(Action):

    def name(self) -> Text:
        return "action_set_status_activity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        id=tracker.current_state()["sender_id"]
        #aggiunta
        associated_name = Database.getName(id)
        activity = tracker.get_slot("activity")
        category = tracker.get_slot("category")
        activity_status = tracker.get_slot("activity_status")
        time = tracker.get_slot("time")

    
        if activity_status == 'completed':
            returnedValue = Database.setItemStatus(id,activity ,category,time,True)
        elif activity_status == 'uncompleted':
            returnedValue = Database.setItemStatus(id,activity ,category,time,False)
        else:
            dispatcher.utter_message(text=f"Ops {associated_name}, I didn't understand what you want to do with this activity") 
            return [SlotSet("activity", None),SlotSet("category", None),SlotSet("time",None),SlotSet("activity_status",None)]

        if (returnedValue):  
            dispatcher.utter_message(text=f"Congratulation {associated_name}, {activity} in {category} set as {activity_status} !") 
        else:
            dispatcher.utter_message(text=f"Ops {associated_name}, this activity does not exists.") 

        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

class actionSetInComplete(Action):

    def name(self) -> Text:
        return "action_set_uncomplete"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        id=tracker.current_state()["sender_id"]
        
        associated_name = Database.getName(id)
        activity = tracker.get_slot("activity")
        category = tracker.get_slot("category")
        time = tracker.get_slot("time")

        returnedValue = Database.setItemStatus(id,activity ,category,time,False)

        if (returnedValue):  
            dispatcher.utter_message(text=f"Congratulation {associated_name}, {activity} in {category} set as incompleted") 
        else:
            dispatcher.utter_message(text=f"Ops {associated_name}, this activity does not exists.") 

        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

class showActivities(Action):
    def name(self) -> Text:
        return "action_view_activities"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        id=tracker.current_state()["sender_id"]
        #aggiunta
        id = 5
        associated_name = Database.getName(id)
        category = tracker.get_slot("category")
        activity_status = tracker.get_slot("activity_status")

        list_of_activity = Database.selectItems(id,category, activity_status)
        dispatcher.utter_message(text=(f"-1 {associated_name} , you have {list_of_activity} activities" if list_of_activity else " No activities found for you!")) 

        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

class showCategories(Action):
    def name(self) -> Text:
        return "action_view_categories"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        id=tracker.current_state()["sender_id"]
       
        associated_name = Database.getName(id)
        list_of_categories = Database.selectPossessions(id)
        
        dispatcher.utter_message(text=(f"-1 {associated_name} , you have {list_of_categories} category" if list_of_categories else " No categories found for you!")) 

        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

class actionModifyCategory(Action):
    def name(self) -> Text:
        return "action_modify_category"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        id=tracker.current_state()["sender_id"]
    
        associated_name = Database.getName(id)
        category_old = tracker.get_slot("category_old")
        category_new = tracker.get_slot("category_new")
        
        if (Database.doesPossessionExists(id,category_new) == False):

            returnedValue = Database.modifyCategory(id, category_old, category_new)
            if (returnedValue):  
                dispatcher.utter_message(text=f"Congratulation {associated_name}, {category_old} modified in {category_new}") 
            else:
                dispatcher.utter_message(text=f"Ops {associated_name} , the category {category_old} does not exists") 
        else:
            dispatcher.utter_message(text=f"Ops {associated_name} , the {category_new} already exists") 
        
        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]

class actionModifyActivity(Action):
    def name(self) -> Text:
        return "action_modify_activity"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        possibleDeadlineErrorFlag=False
        name = tracker.get_slot("name")
        id=tracker.current_state()["sender_id"]
        category_old = tracker.get_slot("category_old")
        activity_old = tracker.get_slot("activity_old")
        activity_new = tracker.get_slot("activity_new")
        category_new = tracker.get_slot("category_new")
        category = tracker.get_slot("category")
        activity = tracker.get_slot("activity")
        time = tracker.get_slot("time")
      
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
            dispatcher.utter_message(text=f"please insert old and new deadline in the next request to allow me to change the deadline of the activity")
            return [SlotSet("category", None),SlotSet("category_old", None),SlotSet("activity_old", None),SlotSet("category_new", None),SlotSet("activity_new", None),SlotSet("activity", None),SlotSet("time", None)]
    

        if(category_new == None):
            category_new = category
        if(activity_new == None):
            activity_new = activity
      
        if (Database.doesUnfoldingsExists(id,category_new,activity_new,timenew) == False):
            returnedValue = Database.modifyActivity(id, cat_to_modify, act_to_modify, timeold, category_new, activity_new, timenew)
            if (returnedValue):  
                dispatcher.utter_message(text=f"Congratulation {associated_name}, the activity {act_to_modify} has been updated") 
            else:
                dispatcher.utter_message(text=f"Ops {associated_name} , the activity to be updated does not exists.") 
        else:
            dispatcher.utter_message(text=f"Ops {associated_name} the  activity {act_to_modify} already exists, it makes no sense to update that") 
    
        return [SlotSet("activity", None),SlotSet("activity_old", None),SlotSet("activity_new", None),SlotSet("category", None),SlotSet("category_old", None),SlotSet("category_new", None),SlotSet("time",None),SlotSet("activity_status",None)]


class actionSetReminderSlot(Action):
    def name(self) -> Text:
        return "action_set_reminder_slot"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("reminder",True)]


class actionCleanCompletedActivities(Action):
    def name(self) -> Text:
        return "action_clean_all_completed"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        id=tracker.current_state()["sender_id"] 
       
        associated_name = Database.getName(id)         
        
        returnedValue = Database.cleanCompletedActivities(id)
        if (returnedValue):  
            dispatcher.utter_message(text=f"Congratulation {associated_name}, I've removed all you completed activity") 
        else:
            dispatcher.utter_message(text=f"Ops! {associated_name} something went wrong! I dont know, check it !") #??
    
        return []

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



class actionRemindItem(Action):
    def name(self) -> Text:
        return "action_reminder_item"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        id=tracker.current_state()["sender_id"]
        activity = tracker.get_slot("activity")
        category = tracker.get_slot("category")
        reminderSlot = tracker.get_slot("reminder")
        time = tracker.get_slot("time")
        id = 5
        associated_name = Database.getName(id) 
        date = datetime.now() + timedelta(seconds = 120)
        entities = [{'name':associated_name, 'activity':activity, 'category':category,'time':time}]
        reminder = ReminderScheduled(
            "EXTERNAL_reminder",
            trigger_date_time = date,
            entities = entities,
            kill_on_user_message = False,
        )

        if (Database.doesUnfoldingsExists(id,category,activity,time)):
            
            returnedValue = Database.updateReminder(id,category,activity,time,reminderSlot)
            if (returnedValue):
                dispatcher.utter_message(text=f"Activity Updated!")
            else:
                dispatcher.utter_message(text=f"{associated_name}, some problem with the update occurred!")
        else:
            actionAddItem.run(self,dispatcher,tracker,domain)
        
        #aggiunte per reminder
        return [SlotSet("activity",None), SlotSet("time",None), SlotSet("category",None),SlotSet("reminder",False),reminder]
        



class actionAskCategoryOld(Action):
    def name(self) -> Text:
        return "action_ask_category_old"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        category_old = tracker.get_slot("category_old")
        category = tracker.get_slot("category")
        if(category_old == None and category == None):
            dispatcher.utter_message(text=f"Please insert the category to be modified")
            return[SlotSet("requested_slot","category")]
        else:
            dispatcher.utter_message(text=f"Please insert the category new")
            return[SlotSet("category_old",category),SlotSet("category",None),SlotSet("category_new",None),SlotSet("requested_slot","category")]    
        


class actionAskCategoryNew(Action):
    def name(self) -> Text:
        return "action_ask_category_new"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        category_new = tracker.get_slot("category_new")
        category = tracker.get_slot("category")
        if(category_new == None and category == None):
            dispatcher.utter_message(text=f"Please insert the category new")
            return[SlotSet("requested_slot","category")]
        else:
            return[SlotSet("category_new",category),SlotSet("category",None),SlotSet("requested_slot",None)]    
        

class actionAskActivityOld(Action):
    def name(self) -> Text:
        return "action_ask_activity_old"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        activity_old = tracker.get_slot("activity_old")
        activity = tracker.get_slot("activity")
        if(activity_old == None and activity == None):
            dispatcher.utter_message(text=f"Please insert the activity to be modified")
            return[SlotSet("requested_slot","activity")]
        else:
            dispatcher.utter_message(text=f"Please insert the activity new")
            return[SlotSet("activity_old",activity),SlotSet("activity",None),SlotSet("activity_new",None),SlotSet("requested_slot","activity")]    

class actionAskActivityNew(Action):
    def name(self) -> Text:
        return "action_ask_activity_new"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        activity_new = tracker.get_slot("activity_new")
        activity = tracker.get_slot("activity")
        if(activity_new == None and activity == None):
            dispatcher.utter_message(text=f"Please insert the activity new")
            return[SlotSet("requested_slot","activity")]
        else:
            return[SlotSet("activity_new",activity),SlotSet("activity",None),SlotSet("requested_slot",None)]    
        



class actionDefaultFallBack(Action):
    def name(self) -> Text:
        return "my_action_fallback"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"Sorry, I lost my mind!")    
        return [SlotSet("activity_old",None),
        SlotSet("activity",None),
        SlotSet("category_old",None),
        SlotSet("category",None),
        SlotSet("time",None),
        SlotSet("activity_status",None),
        SlotSet("activity_new",None),
        SlotSet("category_new",None)]


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
        activity = entities['activity']
        category = entities['category']
        # time = entities['time']
        # time = datetime.fromisoformat(time)
        # date = datetime.now()
        # if time <= date:
        #     dispatcher.utter_message(f"Hei {name}, the reminder  for {activity} in {category} is expired!!!")
        # else:
        #     dispatcher.utter_message(f"Hei {name}, remember to {activity} in {category} in 5 minutes!")
        dispatcher.utter_message(f"Hei {name}, remember to {activity} in {category} in 5 minutes!")
        return []