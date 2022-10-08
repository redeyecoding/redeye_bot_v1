import os
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


env_path = Path('.') / '.env'
load_dotenv()

# Initializes your app with your bot token and signing secret
app = App(token=os.getenv("SLACK_BOT_TOKEN"))


# Add functionality here
# @app.event("app_home_opened") etc


# Start your app

if __name__ == "__main__":
    SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN")).start()

