import os
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
print(f'HERE IS THE TOKEN {os.environ.get("SLACK_BOT_TOKEN")}')

# Initializes your app with your bot token and signing secret
app = App(token=os.environ.get("SLACK_BOT_TOKEN"), signing_secret=os.environ.get("SLACK_SIGNING_SECRET"))


# Add functionality here
# @app.event("app_home_opened") etc


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))

