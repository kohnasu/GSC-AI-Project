from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from slack_bolt.adapter.fastapi import SlackRequestHandler

def create_fastapi_app(slack_app):
    fastapi_app = FastAPI()
    slack_handler = SlackRequestHandler(slack_app)

    @fastapi_app.get("/")
    async def root():
        return HTMLResponse(content="Hello, World!")

    @fastapi_app.post("/slack/events")
    async def slack_events(request: Request):
        body = await request.body()
        print(body)
        if body.get("type") == "url_verification":
            return {"challenge": body.get("challenge")}
        return await slack_handler.handle(request)
    
    return fastapi_app