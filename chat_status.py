from enum import Enum
from utils import today_str, str_to_date
from firebase.models import TABLE_NAMES, add_user_status
from firebase.db import db

class ChatStatus(Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

def judge_chat_status(user_status: dict):
    if user_status.get("start_time") is None:
        return ChatStatus.NOT_STARTED
    if user_status.get("end_time") is None:
        return ChatStatus.IN_PROGRESS
    return ChatStatus.COMPLETED

def check_chat_status(user_id: str, channel_id: str):
    today = today_str()
    doc_ref = db.collection(TABLE_NAMES[1]).document(f"{user_id}_{channel_id}_{today}")
    if doc_ref.get().exists:
        user_status = doc_ref.get().to_dict()
        return user_status.get("day"), judge_chat_status(user_status)
    else:
        query = (
            db.collection(TABLE_NAMES[1])
            .filter("user_id", "==", user_id)
            .filter("channel_id", "==", channel_id)
        )
        docs = query.get()
        docs = [doc.to_dict() for doc in docs]
        if len(docs) == 0:
            add_user_status({
                "user_id": user_id,
                "channel_id": channel_id,
                "date": today,
                "day": 1,
                "start_time": None,
                "end_time": None,
            })
            return 1, ChatStatus.NOT_STARTED
        else:
            day = max([doc.get("day") for doc in docs]) + 1
            add_user_status({
                "user_id": user_id,
                "channel_id": channel_id,
                "date": today,
                "day": day,
                "start_time": None,
                "end_time": None,
            })
            return day, ChatStatus.NOT_STARTED