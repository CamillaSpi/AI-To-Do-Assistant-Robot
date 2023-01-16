#!/usr/bin/env python3
"""

"""
import rospy
from std_msgs.msg import String
from rasa_ros.srv import Dialogue, DialogueResponse
from ros_audio_pkg.msg import RecognizedSpoke
import time

                                           


dialogue_service = rospy.ServiceProxy('dialogue_server', Dialogue)
def testFunction():
    message = RecognizedSpoke()  
    message.msg = "Hi i am Vito"
    message.id = 5
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "aggiungi correre in palestra"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "no"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "modifica il nome dell'attivita correre in palestra con il nome camminare"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "no"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "imposta camminare in palestra come completata"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "no"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "imposta camminare in palestra come incompleta"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "no"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "aggiungi la categoria personale"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "modifica la categoria personale nella categoria universita"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "si"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "rimuovi la categoria universita"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "si"
    dialogue_service(message.msg,message.id) 
    message.msg = "rimuovi le attivita completate"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "si"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "mostra le mie attivita"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "mostra le mie categorie"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "ricordami di chiamare john in personale per ieri"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "rimuovi camminare in palestra"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "no"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "si"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "aggiungi studiare in personale per oggi"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "no"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "modifica il nome dell'attivita chiamata studiare in personale con il nome giocare"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "si"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "oggi"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "modifica la scadenza dell'attivita giocare in personale"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "da oggi a ora"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "ricordami di respirare in personale in 20 secondi"
    dialogue_service(message.msg,message.id) 




def main():
    rospy.init_node('writing')
    rospy.wait_for_service('dialogue_server')
    testFunction()
    message = RecognizedSpoke()  
    message.msg = "/session_start"
    message.id = -1
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)


    while not rospy.is_shutdown():
        message = rospy.wait_for_message("text2answer",RecognizedSpoke)
        print("messaggio arrivato nel dialogue interface: ", message)
        if message == 'exit': 
            break
        try:
            dialogue_service(message.msg,message.id)
            rospy.loginfo('risposta ricevuta')
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

if __name__ == '__main__':
    try: 
        main()
    except rospy.ROSInterruptException:
        pass