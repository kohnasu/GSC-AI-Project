from dotenv import load_dotenv
import os
from slack_app import create_slack_app
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

slack_app = create_slack_app(os.getenv("MANAGER_LOCAL_BOT_USER_OAUTH_TOKEN"), os.getenv("MANAGER_LOCAL_SIGNING_SECRET"))
handler = SocketModeHandler(slack_app, os.getenv("MANAGER_LOCAL_APP_LEVEL_TOKEN"))
handler.start()