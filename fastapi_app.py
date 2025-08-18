import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from slack_bolt.adapter.fastapi import SlackRequestHandler
import logging
import traceback

logger = logging.getLogger(__name__)

def create_fastapi_app(slack_app):
    fastapi_app = FastAPI()
    slack_handler = SlackRequestHandler(slack_app)

    @fastapi_app.get("/")
    async def root():
        return HTMLResponse(content="Hello, World!")
    
    @fastapi_app.get("/health")
    async def health_check():
        return {"status": "healthy", "service": "gsc-ai-project"}
    
    @fastapi_app.get("/ready")
    async def ready_check():
        try:
            if slack_app:
                return {"status": "ready", "slack_app": "initialized"}
            else:
                return {"status": "not_ready", "slack_app": "not_initialized"}
        except Exception as e:
            return {"status": "error", "error": str(e)}


    @fastapi_app.post("/slack/events")
    async def slack_events(request: Request):
        try:
            body = await request.body()
            logger.info(f"Received Slack event: {body}")
            
            try:
                body_json = json.loads(body)
                logger.info(f"Parsed body: {body_json}")
                
                # URL検証の場合
                if body_json.get("type") == "url_verification":
                    challenge = body_json.get("challenge")
                    logger.info(f"URL verification challenge: {challenge}")
                    return {"challenge": challenge}
                
                # その他のSlackイベント
                return await slack_handler.handle(request)
                
            except json.JSONDecodeError as e:
                logger.error(f"JSON decode error: {e}")
                return {"error": "Invalid JSON"}
                
        except Exception as e:
            logger.error(f"Slack events error: {e}")
            logger.error(f"Traceback: {traceback.format_exc()}")
            return {"error": "Internal server error"}
    
    return fastapi_app