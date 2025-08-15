from firebase.db import db
from pydantic import BaseModel
import logging

TABLE_NAMES = ["user","user_status","chatdata"]

logger = logging.getLogger(__name__)

class User(BaseModel):
    user_id: str
    channel_id: str
    email: str | None = None
    display_name: str | None = None
    real_name: str | None = None
    schedule: dict | None = None

class UserStatus(BaseModel):
    user_id: str
    channel_id: str
    date: str # %Y-%m-%d
    day: int
    start_time: float | None = None
    end_time: float | None = None

class ChatData(BaseModel):
    user_id: str
    channel_id: str
    content: str
    day: int
    timestamp: float

## TEMPLATES ##
def add_user(user: dict):
    user = User(**user)
    TABLE_NAME = TABLE_NAMES[0]
    doc_id = f"{user.user_id}_{user.channel_id}"
    doc_ref = db.collection(TABLE_NAME).document(doc_id)
    if doc_ref.get().exists:
        logger.warning(f"User {user.user_id} already exists in {user.channel_id}")
        return
    doc_ref.set(user.model_dump())

def change_user(user: dict):
    user = User(**user)
    TABLE_NAME = TABLE_NAMES[0]
    doc_id = f"{user.user_id}_{user.channel_id}"
    doc_ref = db.collection(TABLE_NAME).document(doc_id)
    if not doc_ref.get().exists:
        logger.warning(f"User {user.user_id} does not exist in {user.channel_id}")
        return
    doc_ref.update(user.model_dump())

def delete_user(user_id: str, channel_id: str):
    TABLE_NAME = TABLE_NAMES[0]
    doc_id = f"{user_id}_{channel_id}"
    doc_ref = db.collection(TABLE_NAME).document(doc_id)
    if not doc_ref.get().exists:
        logger.warning(f"User {user_id} does not exist in {channel_id}")
        return
    doc_ref.delete()

def get_user(user_id: str, channel_id: str):
    TABLE_NAME = TABLE_NAMES[0]
    doc_id = f"{user_id}_{channel_id}"
    doc_ref = db.collection(TABLE_NAME).document(doc_id)
    if not doc_ref.get().exists:
        logger.warning(f"User {user_id} does not exist in {channel_id}")
        return
    return doc_ref.get().to_dict()

def add_user_status(user_status: dict):
    user_status = UserStatus(**user_status)
    TABLE_NAME = TABLE_NAMES[1]
    doc_id = f"{user_status.user_id}_{user_status.channel_id}_{user_status.date}"
    doc_ref = db.collection(TABLE_NAME).document(doc_id)
    if doc_ref.get().exists:
        logger.warning(f"User status {doc_id} already exists")
        return
    doc_ref.set(user_status.model_dump())

def change_user_status(user_status: dict):
    user_status = UserStatus(**user_status)
    TABLE_NAME = TABLE_NAMES[1]
    doc_id = f"{user_status.user_id}_{user_status.channel_id}_{user_status.date}"
    doc_ref = db.collection(TABLE_NAME).document(doc_id)
    if not doc_ref.get().exists:
        logger.warning(f"User status {doc_id} does not exist")
        return
    doc_ref.update(user_status.model_dump())

def delete_user_status(user_id: str, channel_id: str, date: str):
    TABLE_NAME = TABLE_NAMES[1]
    doc_id = f"{user_id}_{channel_id}_{date}"
    doc_ref = db.collection(TABLE_NAME).document(doc_id)
    if not doc_ref.get().exists:
        logger.warning(f"User status {doc_id} does not exist")
        return
    doc_ref.delete()

def get_user_status(user_id: str, channel_id: str, date: str):
    TABLE_NAME = TABLE_NAMES[1]
    doc_id = f"{user_id}_{channel_id}_{date}"
    doc_ref = db.collection(TABLE_NAME).document(doc_id)
    if not doc_ref.get().exists:
        logger.warning(f"User status {doc_id} does not exist")
        return
    return doc_ref.get().to_dict()

def add_chatdata(chatdata: dict):
    chatdata = ChatData(**chatdata)
    TABLE_NAME = TABLE_NAMES[2]
    db.collection(TABLE_NAME).document().set(chatdata.model_dump())

def get_chatdata(user_id: str, channel_id: str, day: int):
    TABLE_NAME = TABLE_NAMES[2]
    query = (
        db.collection(TABLE_NAME)
        .filter("user_id", "==", user_id)
        .filter("channel_id", "==", channel_id)
        .filter("day", "==", day)
    )
    docs = query.get()
    if not docs:
        logger.warning(f"Chatdata {user_id}_{channel_id}_{day} does not exist")
        return []

    return [doc.to_dict() for doc in docs]
