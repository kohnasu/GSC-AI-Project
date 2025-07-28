############################## edit here ##############################################

partner_bot.name = "Partner"
partner_bot.persona = "心優しく親切な性格"
prompt = f"あなたはuserの対話相手で{partner_bot.persona}の{partner_bot.name}です。"

############################## edit here ##############################################

# how to use
# 1. edit prompt (if you want)
# 2. start the app by putting in terminal "python3 main.py -l"
# 3. stop the app by pushing "ctrl + C" while selecting terminal

from slack_bolt import App 
from slack_bolt.adapter.socket_mode import SocketModeHandler
import logging
from collections import defaultdict
from llm import get_response
from SlackBot import partner_bot

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_slack_app(token: str, signing_secret: str):
    app = App(token=token, signing_secret=signing_secret)
    app.chatlog_cache = defaultdict(list)

    # すべてのイベントをログに出力
    @app.middleware
    def log_request(logger, body, next):
        logger.info(f"Received event: {body.get('event', {}).get('type', 'unknown')}")
        logger.info(f"Full body: {body}")
        return next()

    @app.event("message")
    def handle_message_event(message, say):
        logger.info(f"Received message: {message}")
        if message.get("bot_id"):
            logger.info("Ignoring bot message")
            return
        
        user_text = message.get("text")
        channel = message.get("channel")
        logger.info(f"Processing message from channel {channel}: {user_text}")
        if app.chatlog_cache[channel] == []:
            app.chatlog_cache[channel] = [{"role": "developer", "content": prompt}]
        app.chatlog_cache[channel].append({"role": "user", "content": user_text})
        
        llm_response = get_response(app.chatlog_cache[channel])
        partner_bot.response(channel, llm_response)
        app.chatlog_cache[channel].append({"role": "assistant", "content": llm_response})
    return app