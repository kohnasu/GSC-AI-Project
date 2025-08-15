from dotenv import load_dotenv
from fastapi_app import create_fastapi_app
from slack_app import create_slack_app
import os


load_dotenv()

slack_app = create_slack_app(os.getenv("SHIKAISHA_BOT_USER_OAUTH_TOKEN"), os.getenv("SHIKAISHA_SIGNING_SECRET"))
app = create_fastapi_app(slack_app)