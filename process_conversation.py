import time 
from firebase.models import TABLE_NAMES, ChatData
from firebase.db import db
import logging

logger = logging.getLogger(__name__)

def add_chatdata(user_id: str, channel_id: str, content: str, day: int):
    timestamp = time.time()
    cd = ChatData(user_id=user_id, channel_id=channel_id, content=content, day=day, timestamp=timestamp)
    TABLE_NAME = TABLE_NAMES[2]
    db.collection(TABLE_NAME).document().set(cd.model_dump())
    return

def get_chatdata(channel_id: str, day: int):
    TABLE_NAME = TABLE_NAMES[2]
    query = (
        db.collection(TABLE_NAME)
        .where("channel_id", "==", channel_id)
        .where("day", "==", day)
    )
    docs = query.get()
    if not docs:
        logger.warning(f"Chat data does not exist for {channel_id} on day {day}")
        return []
    docs = [doc.to_dict() for doc in docs]
    docs.sort(key=lambda x: x["timestamp"])
    return docs
