from slack_sdk import WebClient
from dotenv import load_dotenv
import os
load_dotenv()

class SlackBot:
    def __init__(self,
        bot_user_oauth_token: str|None=None,
        client_id: str|None=None,
        client_secret: str|None=None,
        signing_secret: str|None=None,
        verification_token: str|None=None,
        app_level_token: str|None=None,
        name: str|None=None,
        persona: str|None=None,
    ):
        self.bot_user_oauth_token = bot_user_oauth_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.signing_secret = signing_secret
        self.verification_token = verification_token
        self.app_level_token = app_level_token
        self.name = name
        self.persona = persona
        
    @property
    def client(self):
        if not self.bot_user_oauth_token:
            raise ValueError("bot_user_oauth_token is required")
        return WebClient(self.bot_user_oauth_token)

    def response(self,channel: str, text: str):
        if not self.client:
            raise ValueError("client is required")
        return self.client.chat_postMessage(
            channel=channel,
            text=text,
        )

partner_bot = SlackBot(
    bot_user_oauth_token=os.getenv("PARTNER_BOT_USER_OAUTH_TOKEN", None),
    client_id=os.getenv("PARTNER_CLIENT_ID", None),
    client_secret=os.getenv("PARTNER_CLIENT_SECRET", None),
    signing_secret=os.getenv("PARTNER_SIGNING_SECRET", None),
    verification_token=os.getenv("PARTNER_VERIFICATION_TOKEN", None),
    app_level_token=os.getenv("PARTNER_APP_LEVEL_TOKEN", None),
)

ren = SlackBot(
    bot_user_oauth_token=os.getenv("REN_BOT_USER_OAUTH_TOKEN", None),
    client_id=os.getenv("REN_CLIENT_ID", None),
    client_secret=os.getenv("REN_CLIENT_SECRET", None),
    signing_secret=os.getenv("REN_SIGNING_SECRET", None),
    verification_token=os.getenv("REN_VERIFICATION_TOKEN", None),
    app_level_token=os.getenv("REN_APP_LEVEL_TOKEN", None),
)

nagi = SlackBot(
    bot_user_oauth_token=os.getenv("NAGI_BOT_USER_OAUTH_TOKEN", None),
    client_id=os.getenv("NAGI_CLIENT_ID", None),
    client_secret=os.getenv("NAGI_CLIENT_SECRET", None),
    signing_secret=os.getenv("NAGI_SIGNING_SECRET", None),
    verification_token=os.getenv("NAGI_VERIFICATION_TOKEN", None),
    app_level_token=os.getenv("NAGI_APP_LEVEL_TOKEN", None),
)