from dotenv import load_dotenv
from fastapi_app import create_fastapi_app
from slack_app import create_slack_app
import os
import uvicorn

load_dotenv()

slack_app = create_slack_app(os.getenv("SHIKAISHA_BOT_USER_OAUTH_TOKEN"), os.getenv("SHIKAISHA_SIGNING_SECRET"))
app = create_fastapi_app(slack_app)

if __name__ == "__main__":
    # Cloud Run用の設定
    port = int(os.getenv("PORT", 8080))
    host = "0.0.0.0"  # すべてのインターフェースでリッスン
    
    uvicorn.run(app, host=host, port=port)