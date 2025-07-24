from dotenv import load_dotenv
import argparse
from slack_app import create_slack_app
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os


load_dotenv()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--local", action="store_true", help="run in local mode")
    args = parser.parse_args()

    if args.local:
        app = create_slack_app(os.getenv("MANAGER_LOCAL_BOT_USER_OAUTH_TOKEN"), os.getenv("MANAGER_LOCAL_SIGNING_SECRET"))
        handler = SocketModeHandler(app, os.getenv("MANAGER_LOCAL_APP_LEVEL_TOKEN"))
        handler.start()
    else:
        raise NotImplementedError("Not implemented")