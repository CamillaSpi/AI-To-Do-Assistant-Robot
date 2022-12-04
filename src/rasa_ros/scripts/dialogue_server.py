#!/usr/bin/env python3
from rasa_ros.srv import Dialogue, DialogueResponse

import rospy
import requests


def handle_service(req):
    input_text = req.input_text
    id = req.id
    # # Get answer        
    get_answer_url = 'http://localhost:5002/webhooks/rest/webhook'
    message = {
        "sender": id,
        "message": input_text
    }

    r = requests.post(get_answer_url, json=message)
    response = DialogueResponse()
    response.answer = ""
    for i in r.json():
        response.answer += i['text'] + ' ' if 'text' in i else ''
    print(response)
    return response

def main():

    # Server Initialization
    rospy.init_node('dialogue_service')

    s = rospy.Service('dialogue_server',
                        Dialogue, handle_service)

    dialogue = Dialogue()  
    dialogue.input_text = "Hi i am Vito"
    dialogue.id = 5
    handle_service(dialogue)
    dialogue = Dialogue()  
    dialogue.input_text = "add run in gym"
    dialogue.id = 5
    handle_service(dialogue)
    dialogue = Dialogue()  
    dialogue.input_text = "no"
    dialogue.id = 5
    handle_service(dialogue)
    dialogue = Dialogue()  
    dialogue.input_text = "yes"
    dialogue.id = 5
    handle_service(dialogue)
    dialogue = Dialogue()  
    dialogue.input_text = "show my activities"
    dialogue.id = 5
    handle_service(dialogue)
    dialogue = Dialogue()  
    dialogue.input_text = "remove run in gym"
    dialogue.id = 5
    handle_service(dialogue)
    dialogue = Dialogue()  
    dialogue.input_text = "no"
    dialogue.id = 5
    handle_service(dialogue)
    dialogue = Dialogue()  
    dialogue.input_text = "modify the category gym into personal"
    dialogue.id = 5
    handle_service(dialogue)
    dialogue = Dialogue()  
    dialogue.input_text = "yes"
    dialogue.id = 5
    handle_service(dialogue)
    dialogue = Dialogue()  
    dialogue.input_text = "show my categories"
    dialogue.id = 5
    handle_service(dialogue)
    rospy.logdebug('Dialogue server READY.')
    rospy.spin()


if __name__ == '__main__':
    try: 
        main()
    except rospy.ROSInterruptException as e:
        pass
