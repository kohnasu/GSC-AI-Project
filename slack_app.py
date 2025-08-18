
# how to use
# 1. edit prompt (if you want)
# 2. start the app by putting in terminal "python3 main.py -l"
# 3. stop the app by pushing "ctrl + C" while selecting terminal

from slack_bolt import App 
from slack_bolt.adapter.socket_mode import SocketModeHandler
import logging
from llm import get_response
from SlackBot import ren, nagi
from firebase.db import db
from mockdata import persona, name, topic

from check_register_user import check_user_exists, register_user
from chat_status import ChatStatus, check_chat_status, start_chat, end_chat 
from process_conversation import add_chatdata, get_chatdata

chatbots = {
    "nagi": {
        "chatbot": nagi,
        "user_id": "U09A12GDEEP",
    },
    "ren": {
        "chatbot": ren,
        "user_id": "U09AAKK4KMJ",
    },
}

chatbot_map = {
    "U09A12GDEE": nagi,
    "U09AAKK4KMJ": ren,
}

nagi.user_id = "U09A12GDEEP"
ren.user_id = "U09AAKK4KMJ"


# ログ設定
############################## edit here ##############################################

ren.name = "蓮"
ren.persona = "心優しく親切な性格"

nagi.name = "凪"
nagi.persona = "心優しく親切な性格"

current_bot = ren

PERSONALITY_TEMPLATE = "あなたは{username}の対話相手で{persona}の{name}です。\n"
CHATLOG_TEMPLATE = "[{name}] {content}\n"

PROMPT_TEMPLATE = """{personality}。
これまでの会話の流れに沿うように応答してください。
[]内の名前は含めないでください。

これまでの会話の流れ:
{chatlog}

"""

############################## edit here ##############################################
def create_chatlog(user_id: str, username: str, channel: str, day: int):
    if username is None:
        username = "user"
    chatlog = ""
    chatdatas = get_chatdata(channel, day)
    for chatdata in chatdatas:
        if chatdata["user_id"] == user_id:
            chatlog += CHATLOG_TEMPLATE.format(name=username, content=chatdata["content"])
        elif chatdata["user_id"] in chatbot_map:
            chatlog += CHATLOG_TEMPLATE.format(name=chatbot_map[chatdata["user_id"]].name, content=chatdata["content"])
        else:
            logger.warning(f"Unknown user {chatdata['user_id']} in chatlog")
    return chatlog

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_slack_app(token: str, signing_secret: str):
    app = App(token=token, signing_secret=signing_secret)
    
    # # FastAPI用の設定
    # app.logger = logger

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
            if status == ChatStatus.COMPLETED:
                say("本日のチャットは終了しています")
                return
            if status == ChatStatus.IN_PROGRESS:
                if user_text == "チャット終了":
                    end_chat(user_id, channel)
                    say(text="チャットを終了しました")
                    return
            # チャット進行中
                username = user_data.get("user", {}).get("profile", {}).get("display_name", None) or user_data.get("user", {}).get("profile", {}).get("real_name", None)
                add_chatdata(user_id, channel, user_text, day)
                chatlog = create_chatlog(user_id, username, channel, day)
                prompt = PROMPT_TEMPLATE.format(personality=PERSONALITY_TEMPLATE.format(username=username, persona=current_bot.persona, name=current_bot.name), chatlog=chatlog)
                logger.info(f"Prompt: {prompt}")
                llm_response = get_response(prompt)
                current_bot.response(channel, llm_response)
                add_chatdata(current_bot.user_id, channel, llm_response, day)
                return
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}")
            try:
                say(text="申し訳ございません。エラーが発生しました。")
            except:
                logger.error("Could not send error message to user")
    return app