from dotenv import load_dotenv
import os
from slack_app import create_slack_app, create_slack_app_test
from slack_bolt.adapter.socket_mode import SocketModeHandler
import argparse

load_dotenv()
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", action="store_true", default=False, help="テストモードで起動します")
args = parser.parse_args()

if args.test:
    print("テストモードで起動します")
    test_slack_app = create_slack_app_test(os.getenv("MANAGER_LOCAL_BOT_USER_OAUTH_TOKEN"), os.getenv("MANAGER_LOCAL_SIGNING_SECRET"))
    test_handler = SocketModeHandler(test_slack_app, os.getenv("MANAGER_LOCAL_APP_LEVEL_TOKEN"))
    test_handler.start()
else:
    print("本番モードで起動します")
    slack_app = create_slack_app(os.getenv("MANAGER_LOCAL_BOT_USER_OAUTH_TOKEN"), os.getenv("MANAGER_LOCAL_SIGNING_SECRET"))
    handler = SocketModeHandler(slack_app, os.getenv("MANAGER_LOCAL_APP_LEVEL_TOKEN"))
    handler.start()