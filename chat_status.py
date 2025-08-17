from enum import Enum
import time
from utils import today_str, str_to_date
from firebase.models import TABLE_NAMES, add_user_status
from firebase.db import db
import logging

logger = logging.getLogger(__name__)

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
            .where("user_id", "==", user_id)
            .where("channel_id", "==", channel_id)
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

def start_chat(user_id: str, channel_id: str):
    try:
        today = today_str()
        doc_ref = db.collection(TABLE_NAMES[1]).document(f"{user_id}_{channel_id}_{today}")
        if not doc_ref.get().exists:
            logger.error(f"User {user_id} does not exist in {channel_id}")
            return None, None
        doc_ref.update({
            "start_time": time.time(),
        })
        day = doc_ref.get().to_dict().get("day")
        return day, ChatStatus.IN_PROGRESS
    except Exception as e:
        logger.error(f"Chat start error: {e}")
        return None, None

def end_chat(user_id: str, channel_id: str):
    try:
        today = today_str()
        doc_ref = db.collection(TABLE_NAMES[1]).document(f"{user_id}_{channel_id}_{today}")
        if not doc_ref.get().exists:
            logger.error(f"User {user_id} does not exist in {channel_id}")
            return
        doc_ref.update({
            "end_time": time.time(),
        })
        return doc_ref.get().to_dict().get("day"), ChatStatus.COMPLETED
    except Exception as e:
        logger.error(f"Chat end error: {e}")
        return None, None