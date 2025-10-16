from config import YUGO_USER_ID, KOH_USER_ID
from SlackBot import ren, nagi, hibiki, yuki, chihiro, nagisa
import logging

setting_attrs = ["day", "topic_name", "user_position", "bot_position", "bot", "bot_name", "bot_persona", "first_message"]

logger = logging.getLogger(__name__)

SETTINGS = [
    {
        "user_id": YUGO_USER_ID,
        "settings": [
            {
                "day": 1,
                "topic_name": "理系と文系どちらが嬉しいか",
                "user_position": "理系",
                "bot_position": "共感",
                "bot": ren,
                "bot_name": "蓮",
                "bot_persona": "理系として活動してるけど文系がいいと思っている",
                "first_message": "こんにちは！どうしたのかな？話したいことがあれば教えてね。",
            },
            {
                "day": 2,
                "topic_name": "犬派と猫派どちらが好きか",
                "user_position": "犬派",
                "bot_position": "否定",
                "bot": nagi,
                "bot_name": "凪",
                "bot_persona": "猫派で猫の魅力を熱く語る",
                "first_message": "こんにちは！どうしたのかな？話したいことがあれば教えてね。",
            },
            {
                "day": 3,
                "topic_name": "朝型と夜型どちらが良いか",
                "user_position": "夜型",
                "bot_position": "共感",
                "bot": hibiki,
                "bot_name": "響",
                "bot_persona": "夜型で夜の静けさが好き",
                "first_message": "こんにちは！どうしたのかな？話したいことがあれば教えてね。",
            },
            {
                "day": 4,
                "topic_name": "都会と田舎どちらに住みたいか",
                "user_position": "都会",
                "bot_position": "否定",
                "bot": yuki,
                "bot_name": "雪",
                "bot_persona": "田舎の自然や静けさを推す",
                "first_message": "こんにちは！どうしたのかな？話したいことがあれば教えてね。",
            },
            {
                "day": 5,
                "topic_name": "和食と洋食どちらが好きか",
                "user_position": "洋食",
                "bot_position": "共感",
                "bot": chihiro,
                "bot_name": "千尋",
                "bot_persona": "洋食好きで色々な国の料理に詳しい",
                "first_message": "こんにちは！どうしたのかな？話したいことがあれば教えてね。",
            },
            {
                "day": 6,
                "topic_name": "旅行は計画派か行き当たりばったり派か",
                "user_position": "計画派",
                "bot_position": "否定",
                "bot": nagisa,
                "bot_name": "渚",
                "bot_persona": "行き当たりばったりの旅の楽しさを語る",
                "first_message": "こんにちは！どうしたのかな？話したいことがあれば教えてね。",
            },
        ]
    },
    {
        "user_id": KOH_USER_ID,
        "settings": [
            {
                "day": 1,
                "topic_name": "理系と文系どちらが嬉しいか",
                "user_position": "理系",
                "bot_position": "共感",
                "bot": ren,
                "bot_name": "蓮",
                "bot_persona": "理系として活動してるけど文系がいいと思っている",
                "first_message": "こんにちは！どうしたのかな？話したいことがあれば教えてね。",
            },
            {
                "day": 2,
                "topic_name": "犬派と猫派どちらが好きか",
                "user_position": "犬派",
                "bot_position": "否定",
                "bot": nagi,
                "bot_name": "凪",
                "bot_persona": "猫派で猫の魅力を熱く語る",
                "first_message": "こんにちは！どうしたのかな？話したいことがあれば教えてね。",
            },
            {
                "day": 3,
                "topic_name": "朝型と夜型どちらが良いか",
                "user_position": "夜型",
                "bot_position": "共感",
                "bot": hibiki,
                "bot_name": "響",
                "bot_persona": "夜型で夜の静けさが好き",
                "first_message": "こんにちは！どうしたのかな？話したいことがあれば教えてね。",
            },
            {
                "day": 4,
                "topic_name": "都会と田舎どちらに住みたいか",
                "user_position": "都会",
                "bot_position": "否定",
                "bot": yuki,
                "bot_name": "雪",
                "bot_persona": "田舎の自然や静けさを推す",
                "first_message": "こんにちは！どうしたのかな？話したいことがあれば教えてね。",
            },
            {
                "day": 5,
                "topic_name": "和食と洋食どちらが好きか",
                "user_position": "洋食",
                "bot_position": "共感",
                "bot": chihiro,
                "bot_name": "千尋",
                "bot_persona": "洋食好きで色々な国の料理に詳しい",
                "first_message": "こんにちは！どうしたのかな？話したいことがあれば教えてね。",
            },
            {
                "day": 6,
                "topic_name": "旅行は計画派か行き当たりばったり派か",
                "user_position": "計画派",
                "bot_position": "否定",
                "bot": nagisa,
                "bot_name": "渚",
                "bot_persona": "行き当たりばったりの旅の楽しさを語る",
                "first_message": "こんにちは！どうしたのかな？話したいことがあれば教えてね。",
            },
        ]
    },
]


def check_settings(user_id: str):
    for s in SETTINGS:
        if s["user_id"] == user_id:
            settings = s["settings"]
            break
    else:
        logger.error(f"User {user_id} has no settings")
        return False
    days = set(setting.get("day") for setting in settings if "day" in setting)
    if set(range(1, 7)) != days:
        logger.error(f"User {user_id} has incomplete settings")
        return False
    for setting in settings:
        for attr in setting_attrs:
            if setting[attr] is None:
                logger.error(f"User {user_id} has incomplete settings")
                return False
    return True
    
def check_all_settings():
    for s in SETTINGS:
        if not check_settings(s["user_id"]):
            logger.error(f"User {s['user_id']} has incomplete settings")
            return False
    return True


def get_setting(user_id: str, day: int):
    for s in SETTINGS:
        if s["user_id"] == user_id:
            settings = s["settings"]
            break
    else:
        logger.error(f"User {user_id} has no settings")
        return None
    for setting in settings:
        if setting["day"] == day:
            return setting
    else:
        logger.error(f"User {user_id} has no setting for day {day}")
        return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    if check_all_settings():
        logger.info("All settings are complete")
    else:
        logger.error("Some settings are incomplete")