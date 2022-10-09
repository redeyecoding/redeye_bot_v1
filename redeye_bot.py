import os
from pathlib import Path
from dotenv import load_dotenv
from slack import WebClient
from slack.errors import SlackApiError

env_path = Path('.') / '.env'
load_dotenv()

slack_token = os.environ["SLACK_APP_TOKEN"]
client = WebClient(token=slack_token)

# Verify it works
client = WebClient()
api_response = client.api_test()

try:
  response = client.chat_postMessage(
    channel="C0XXXXXX",
    text="Hello from your app! :tada:"
  )
except SlackApiError as e:
  # You will get a SlackApiError if "ok" is False
  assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
