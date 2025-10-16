import os
from datetime import datetime
from firebase.db import db
from firebase.models import TABLE_NAMES

def export_firestore_to_local_storage(date_str=None):
    """
    firestoreの各テーブルの内容をstorage_backup/{date}/配下に保存する
    :param date_str: YYYYMMDD形式の日付文字列。指定しなければ今日の日付を使う
    """
    if date_str is None:
        date_str = datetime.now().strftime("%Y%m%d%H%M")
    backup_dir = os.path.join("storage_backup", date_str)
    os.makedirs(backup_dir, exist_ok=True)

    for table_name in TABLE_NAMES:
        print(f"Exporting table: {table_name}")
        docs = db.collection(table_name).get()
        all_data = [doc.to_dict() for doc in docs]
        export_path = os.path.join(backup_dir, f"{table_name}.json")
        try:
            import json
        except ImportError:
            raise Exception("json module required but cannot import")
        with open(export_path, "w", encoding="utf-8") as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        print(f"Backed up {len(all_data)} documents from {table_name} to {export_path}")


if __name__ == "__main__":
    export_firestore_to_local_storage()
