import concurrent.futures
import time
from firebase.models import TABLE_NAMES, add_user
from firebase.db import db
import logging

logger = logging.getLogger(__name__)

def check_user_exists(message: dict):
    try:
        user_id = message["user"]
        channel_id = message["channel"]
        logger.info(f"Checking user existence for user_id: {user_id}, channel_id: {channel_id}")
    except KeyError:
        logger.warning(f"User or channel not found in message: {message}")
        return False
    
    try:
        doc_id = f"{user_id}_{channel_id}"
        doc_ref = db.collection(TABLE_NAMES[0]).document(doc_id)
        
        # タイムアウト付きでドキュメントを取得
        def get_document():
            try:
                return doc_ref.get()
            except Exception as e:
                logger.error(f"Error in get_document: {e}")
                return None
        
        # 5秒のタイムアウトでドキュメントを取得
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(get_document)
            try:
                doc = future.result(timeout=5.0)
            except concurrent.futures.TimeoutError:
                logger.error("Document retrieval timed out after 5 seconds")
                return False
            except Exception as e:
                logger.error(f"Error retrieving document: {e}")
                return False
        
        if doc and doc.exists:
            return True
        else:
            return False
            
    except Exception as e:
        logger.error(f"Error checking user existence: {e}")
        return False

def register_user(message: dict, user_data: dict):
    user = {
        "user_id": message["user"],
        "channel_id": message["channel"],
        "display_name": user_data.get("user", {}).get("profile", {}).get("display_name", None),
        "real_name": user_data.get("user", {}).get("profile", {}).get("real_name", None),
        "email": user_data.get("user", {}).get("profile", {}).get("email", None),
    }
    add_user(user)
    logger.info(f"User {user['user_id']} registered in {user['channel_id']}")
    return