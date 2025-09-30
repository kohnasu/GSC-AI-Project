
# how to use
# 1. edit prompt (if you want)
# 2. start the app by putting in terminal "python3 local.py"
# 3. stop the app by pushing "ctrl + C" while selecting terminal

from slack_bolt import App 
from slack_bolt.adapter.socket_mode import SocketModeHandler
import logging
from time import time
import pytz
from datetime import datetime

from llm import get_response
from SlackBot import ren, nagi, hibiki, yuki, chihiro, nagisa
from firebase.db import db
from mockdata import persona, name, topic
from config import CAN_FINISH_MINUTES, MUST_FINISH_MINUTES, MINIMUM_TURNS, EVERYDAY_FORM_URL, PERIODIC_FORM_URL

from check_register_user import check_user_exists, register_user
from chat_status import ChatStatus, ChatFinish, check_chat_status, start_chat, end_chat 
from process_conversation import add_chatdata, get_chatdata

chatbot_list = [nagi, ren, hibiki, yuki, chihiro, nagisa]

chatbots = {
    "nagi": {
        "chatbot": nagi,
        "user_id": "U09A12GDEEP",
    },
    "ren": {
        "chatbot": ren,
        "user_id": "U09AAKK4KMJ",
    },
    "hibiki": {
        "chatbot": hibiki,
        "user_id": "U09HD01CNCX",
    },
    "yuki": {
        "chatbot": yuki,
        "user_id": "U09HD17UDPH",
    },
    "chihiro": {
        "chatbot": chihiro,
        "user_id": "U09HSKET7GW",
    },
    "nagisa": {
        "chatbot": nagisa,
        "user_id": "U09HSJVGG06",
    },
}

chatbot_map = {
    "U09A12GDEE": nagi,
    "U09AAKK4KMJ": ren,
    "U09HD01CNCX": hibiki,
    "U09HD17UDPH": yuki,
    "U09HSKET7GW": chihiro,
    "U09HSJVGG06": nagisa,
}

nagi.user_id = "U09A12GDEEP"
ren.user_id = "U09AAKK4KMJ"
hibiki.user_id = "U09HD01CNCX"
yuki.user_id = "U09HD17UDPH"
chihiro.user_id = "U09HSKET7GW"
nagisa.user_id = "U09HSJVGG06"


############################## edit here ##############################################

ren.name = "蓮"
ren.persona = ""

nagi.name = "凪"
nagi.persona = ""

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



def create_chatlog(user_id: str, username: str, chatdatas: list):
    if username is None:
        username = "user"
    chatlog = ""
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
            logger.info(f"User data: {user_data}")
            
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
                    chat_status = check_chat_status(user_id, channel)
                    day = chat_status["day"]
                    status = chat_status["status"]
                    finish = chat_status["finish"]
                    if status == ChatStatus.NOT_STARTED:
                        say(text=f"チャットを開始する前に、以下のフォームに回答してください。\n{EVERYDAY_FORM_URL}")
                        say(text=f"また、{day}日目のチャットを開始するには「チャット開始」と打ってください。")
                        return
                    return
                say(text="このチャンネルでのユーザ登録が済んでいません。「ユーザ登録」と打ってユーザ登録を行ってください。")
                return
            
            chat_status = check_chat_status(user_id, channel)
            day = chat_status["day"]
            status = chat_status["status"]
            finish = chat_status["finish"]
            username = user_data.get("user", {}).get("profile", {}).get("display_name", None) or user_data.get("user", {}).get("profile", {}).get("real_name", None)
            if status == ChatStatus.NOT_STARTED:
                if user_text == "チャット開始":
                    # 日本時間23時以降はチャット開始不可
                    jst = pytz.timezone('Asia/Tokyo')
                    now_jst = datetime.now(jst)
                    if now_jst.hour >= 23:
                        say(text="日本時間23時以降はチャットを開始できません。翌日になってから「チャット開始」と打ってください。")
                        return
                    chat_status = start_chat(user_id, channel)
                    say(text=f"{day}日目のチャットを開始しました")
                    return
                say(text=f"チャットが始まっていません。{day}日目のチャットを開始するには「チャット開始」と打ってください。\nチャット開始するには「チャット開始」と打ってください。また、チャットを終了するには「チャット終了」と打ってください。")
                return
            if status == ChatStatus.COMPLETED:
                say("本日のチャットは終了しています")
                return
            if status == ChatStatus.IN_PROGRESS:
                chatdatas = get_chatdata(channel, day)
                if finish == ChatFinish.MUST_FINISH:
                    comment = f"{MUST_FINISH_MINUTES}分以上チャットしています。チャットを終了します。\n"
                    comment += f"以下のフォームに回答をお願いします。\n{EVERYDAY_FORM_URL}"
                    if day == 3 or day == 6:
                        comment = f"今日は{day}日目です。以下のフォームに回答をお願いします。\n{PERIODIC_FORM_URL}"
                    say(text=comment)
                    end_chat(user_id, channel)
                    return
                if user_text == "チャット終了":
                    if finish == ChatFinish.CAN_FINISH and len(chatdatas) >= MINIMUM_TURNS * 2:
                        comment = f"{CAN_FINISH_MINUTES}分以上チャットしています。チャットを終了します。\n"
                        comment += f"以下のフォームに回答をお願いします。\n{EVERYDAY_FORM_URL}"
                        if day == 3 or day == 6:
                            comment = f"今日は{day}日目です。以下のフォームに回答をお願いします。\n{PERIODIC_FORM_URL}"
                        say(text=comment)
                        end_chat(user_id, channel)
                        return
                    if finish == ChatFinish.NOT_YET:
                        say(text=f"まだ{MINIMUM_TURNS}回以上チャットしていないか、{CAN_FINISH_MINUTES}分以上チャットしていないです。チャットを続けてください。")
                        return
            # チャット進行中
                add_chatdata(user_id, channel, user_text, day)
                chatlog = create_chatlog(user_id, username, chatdatas)
                prompt = PROMPT_TEMPLATE.format(personality=PERSONALITY_TEMPLATE.format(username=username, persona=current_bot.persona, name=current_bot.name),chatlog=chatlog)
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