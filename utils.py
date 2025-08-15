from datetime import datetime

def today_str():
    now = datetime.now()
    return now.isoformat().split("T")[0]

def str_to_date(date_str: str):
    return datetime.fromisoformat(date_str)


if __name__ == "__main__":
    print(today_str())
    print(str_to_date("2025-08-15"))