import os
from pathlib import Path
from dotenv import load_dotenv
import slack
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from flask import Flask

env_path = Path('.') / '.env'
load_dotenv()

app = Flask(__name__)

slack_web_client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
slack_events_adapter = SlackEventAdapter(os.environ.get("SLACK_APP_TOKEN", "/slack/events", app))

MESSAGE_BLOCK = {
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": "",
    },
}


@slack_events_adapter.on("message")
def message(payload):
    event = payload.get("event", {})

    text = event.get("text")

    if "hello redeye" in text.lower():
        channel_id = event.get("channel")
        bot_response_message = "Hello there from redeyebot"

        MESSAGE_BLOCK["text"]["text"] = bot_response_message

        block_package = {
            "channel": channel_id,
            "blocks": [MESSAGE_BLOCK]
        }


    return slack_web_client.chat_postMessage(**block_package)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)