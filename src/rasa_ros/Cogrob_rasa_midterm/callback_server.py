from sanic import Sanic, response
from sanic.request import Request
from sanic.response import HTTPResponse


def create_app() -> Sanic:

    bot_app = Sanic("callback_server", configure_logging=False)

    @bot_app.post("/bot")
    def rospy.loginfo_response(request: Request) -> HTTPResponse:
        """rospy.loginfo bot response to the console."""
        rospy.loginfo('sono nel server')
        bot_response = request.json.get("text")
        rospy.loginfo(f"\n{bot_response}")

        body = {"status": "message sent"}
        return response.json(body, status=200)

    return bot_app


if __name__ == "__main__":
    app = create_app()
    port = 5034

    rospy.loginfo(f"Starting callback server on port {port}.")
    app.run("0.0.0.0", port)
    
