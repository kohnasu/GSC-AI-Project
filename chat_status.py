from enum import Enum
import time
from utils import today_str, str_to_date
from firebase.models import TABLE_NAMES, add_user_status
from firebase.db import db
import logging
from config import CAN_FINISH_MINUTES, MUST_FINISH_MINUTES

logger = logging.getLogger(__name__)

class ChatStatus(Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class ChatFinish(Enum):
    CAN_FINISH = "can_finish"
    NOT_YET = "not_yet"
    MUST_FINISH = "must_finish"


def judge_chat_status(user_status: dict):
    if user_status.get("start_time") is None:
        return ChatStatus.NOT_STARTED
    if user_status.get("end_time") is None:
        return ChatStatus.IN_PROGRESS
    return ChatStatus.COMPLETED

def judge_chat_finish(user_status: dict):
    current_time = time.time()
    start_time = user_status.get("start_time")
    if start_time is None:
        return None
    diff = current_time - start_time
    if diff > MUST_FINISH_MINUTES * 60:
        return ChatFinish.MUST_FINISH
    elif diff > CAN_FINISH_MINUTES * 60:
        return ChatFinish.CAN_FINISH
    return ChatFinish.NOT_YET


def check_chat_status(user_id: str, channel_id: str):
    today = today_str()
    doc_ref = db.collection(TABLE_NAMES[1]).document(f"{user_id}_{channel_id}_{today}")
    if doc_ref.get().exists:
        user_status = doc_ref.get().to_dict()
        day = user_status.get("day")
        status = judge_chat_status(user_status)
        finish = judge_chat_finish(user_status)
        return {
            "day": day,
            "status": status,
            "finish": finish,
        }
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
            return {
                "day": 1,
                "status": ChatStatus.NOT_STARTED,
                "finish": None,
            }
        else:
            for doc in docs:
                if doc.get("start_time") is None:
                    db.collection(TABLE_NAMES[1]).document(doc.get("user_id") + "_" + doc.get("channel_id") + "_" + doc.get("date")).delete()
                continue
            day = max([doc.get("day") for doc in docs],default=0) + 1
            add_user_status({
                "user_id": user_id,
                "channel_id": channel_id,
                "date": today,
                "day": day,
                "start_time": None,
                "end_time": None,
            })
            return {
                "day": day,
                "status": ChatStatus.NOT_STARTED,
                "finish": None,
            }


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
        return {
            "day": day,
            "status": ChatStatus.IN_PROGRESS,
            "finish": None,
        }
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