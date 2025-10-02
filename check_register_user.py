import concurrent.futures
import time
from firebase.models import TABLE_NAMES, add_user
from firebase.db import db
import logging
from enum import Enum
from settings import check_settings, SETTINGS

logger = logging.getLogger(__name__)

class UserRegisterStatus(Enum):
    NOT_REGISTERED = "not_registered"
    NOT_SETTING_DONE = "not_setting_done"
    SETTING_DONE = "setting_done"

def check_user_register_status(user_id: str, channel_id: str):
    try:
        doc_id = f"{user_id}_{channel_id}"
        doc_ref = db.collection(TABLE_NAMES[0]).document(doc_id)
        
        doc = doc_ref.get()
        if doc is None:
            return UserRegisterStatus.NOT_REGISTERED
        if doc.exists:
            user = doc.to_dict()
            if user.get("setting_done"):
                return UserRegisterStatus.SETTING_DONE
            else:
                if check_settings(user_id):
                    doc_ref.update({"setting_done": True})
                    return UserRegisterStatus.SETTING_DONE
                else:
                    return UserRegisterStatus.NOT_SETTING_DONE
        else:
            return UserRegisterStatus.NOT_REGISTERED
            
    except Exception as e:
        logger.error(f"Error checking user existence: {e}")
        return UserRegisterStatus.NOT_REGISTERED

def register_user(message: dict, user_data: dict):
    user = {
        "user_id": message["user"],
        "channel_id": message["channel"],
        "display_name": user_data.get("user", {}).get("profile", {}).get("display_name", None),
        "real_name": user_data.get("user", {}).get("profile", {}).get("real_name", None),
        "email": user_data.get("user", {}).get("profile", {}).get("email", None),
        "setting_done": False,
    }
    add_user(user)
    logger.info(f"User {user['user_id']} registered in {user['channel_id']}")
    return