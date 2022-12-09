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
        """Print bot response to the console."""
        text = request.json.get("text")
        if text[0:2] == '-1':
            pub2.publish(r'http://http://172.19.215.10:80/webPage/')
            text = text[2:]
        elif text[0:2] == '-2':
            pub2.publish(r'http://http://172.19.215.10:80/webPage/')
            text = text[2:]
        pub.publish(text)

        body = {"status": "message sent"}
        return response.json(body, status=200)

    return bot_app
    

def main():
    rospy.init_node('callback')
    app = create_app()
    port = 5034

    print(f"Starting callback server on port {port}.")
    app.run("0.0.0.0", port)


if __name__ == '__main__':
    try: 
        main()
    except rospy.ROSInterruptException as e:
        pass
