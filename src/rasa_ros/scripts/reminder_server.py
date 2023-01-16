#!/usr/bin/env python3
from rasa_ros.srv import Dialogue, DialogueResponse
from sanic import Sanic, response
from sanic.request import Request
from sanic.response import HTTPResponse
import rospy
import requests
from std_msgs.msg import String


pub = rospy.Publisher('toSpeech', String, queue_size=10)
pub2 = rospy.Publisher("toShow", String,  queue_size=10)

def create_app() -> Sanic:

    bot_app = Sanic("callback_server", configure_logging=False)

    @bot_app.post("/bot")
    def print_response(request: Request) -> HTTPResponse:
        """rospy.loginfo bot response to the console."""
        text = request.json.get("text")
        rospy.loginfo(text)
        try:
            json_query = request.json.get('custom')['query']
            print('ho riceuvto ' , json_query)
            if "js" not in json_query:
                pub2.publish(f'http://10.0.1.248:80/webPage/index.php?query={json_query}')
                rospy.loginfo(f'http://10.0.1.248:80/webPage/index.php?query={json_query}')
            else:
                if 'reload' not in json_query:
                    pub2.publish('js')
                    rospy.loginfo('ricevuto js')
                else:
                    pub2.publish('reload')
                    rospy.loginfo('reload')
        except:
            pub.publish(text)

        body = {"status": "message sent"}
        return response.json(body, status=200)

    return bot_app

def handle_service(req):
    input_text = req.input_text
    id = req.id
    print('USER:' , input_text)
    # # Get answer        
    get_answer_url = 'http://localhost:5005/webhooks/callback/webhook'
    message = {
        "sender": id,
        "message": input_text
    }

    r = requests.post(get_answer_url, json=message)
    response = DialogueResponse()
    response.answer = str(r)

    return response
def main():
    rospy.init_node('callback')
    try:
        app = create_app()
        port = 5034
        s = rospy.Service('dialogue_server',
                            Dialogue, handle_service)
        rospy.logdebug('Dialogue server READY.')
        rospy.loginfo(f"Starting callback server on port {port}.")
        app.run("0.0.0.0", port)
        rospy.spin()
    except rospy.ROSInterruptException as e:
        rospy.loginfo(e)
        app.stop()  


if __name__ == '__main__':
    main()
