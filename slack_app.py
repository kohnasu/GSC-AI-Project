
# how to use
# 1. edit prompt (if you want)
# 2. start the app by putting in terminal "python3 main.py -l"
# 3. stop the app by pushing "ctrl + C" while selecting terminal

from slack_bolt import App 
from slack_bolt.adapter.socket_mode import SocketModeHandler
import logging
from collections import defaultdict
from llm import get_response
from SlackBot import partner_bot, ren, nagi
from firebase.db import db
from mockdata import persona, name, topic

from check_register_user import check_user_exists, register_user
from chat_status import ChatStatus, check_chat_status, start_chat


# ログ設定
############################## edit here ##############################################

partner_bot.name = "Partner"
partner_bot.persona = "心優しく親切な性格"

ren.name = "蓮"
ren.persona = "心優しく親切な性格"

nagi.name = "凪"
nagi.persona = "心優しく親切な性格"

current_bot = ren

prompt = f"あなたはuserの対話相手で{partner_bot.persona}の{partner_bot.name}です。"

############################## edit here ##############################################
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_slack_app(token: str, signing_secret: str):
    app = App(token=token, signing_secret=signing_secret)
    app.chatlog_cache = defaultdict(list)

    # すべてのイベントをログに出力
    # @app.middleware
    # def log_request(logger, body, next):
    #     logger.info(f"Received event: {body.get('event', {}).get('type', 'unknown')}")
    #     logger.info(f"Full body: {body}")
    #     return next()

    @app.event("message")
    def handle_message_event(message, say):
        try:
            user_id = message.get("user")
            # logger.info(f"Received message from user {user_id}: {message}")
            user_data = app.client.users_info(user=user_id)
            
            # ボットメッセージは無視
            if message.get("bot_id"):
                logger.info("Ignoring bot message")
                return
            
            channel = message.get("channel")
            user_text = message.get("text")
            logger.info(f"Processing message from channel {channel}: {user_text}")

            # ユーザー存在チェック
            try:
                user_exists = check_user_exists(message)
            except Exception as e:
                logger.error(f"Error in check_user_exists: {e}")
                user_exists = False
            
            if not user_exists:
                if user_text == "ユーザ登録":
                    register_user(message,user_data)
                    say(text="ユーザ登録が完了しました。")
                    return
                say(text="このチャンネルでのユーザ登録が済んでいません。「ユーザ登録」と打ってユーザ登録を行ってください。")
                return
            
            day, status = check_chat_status(user_id, channel)
            if status == ChatStatus.NOT_STARTED:
                if user_text == "チャット開始":
                    day, status = start_chat(user_id, channel)
                    say(text=f"{day}日目のチャットを開始しました")
                    return
                say(text=f"チャットが始まっていません。{day}日目のチャットを開始するには「チャット開始」と打ってください。")
                return
            # ここから
            raise NotImplementedError("Not implemented")
            # LLMからレスポンスを取得
            logger.info("Getting response from LLM...")
            llm_response = get_response(app.chatlog_cache[channel])
            logger.info(f"LLM response: {llm_response}")
            
            # スラックにレスポンスを送信
            logger.info("Sending response to Slack...")
            current_bot.response(channel, llm_response)
            logger.info("Response sent successfully")
            
            app.chatlog_cache[channel].append({"role": "assistant", "content": llm_response})
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}")
            try:
                say(text="申し訳ございません。エラーが発生しました。")
            except:
                logger.error("Could not send error message to user")
    return app