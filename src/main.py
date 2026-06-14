import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request

from src.whatsapp_api import send_message
from src.predefined_responses import RESPONSES

load_dotenv()

app = FastAPI()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")


@app.get("/")
def home():

    return {
        "status": "Atlas Flow Online"
    }


@app.get("/webhook")
async def verify_webhook(request: Request):

    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return int(challenge)

    return {
        "error": "verification failed"
    }


@app.post("/webhook")
async def receive_message(request: Request):

    data = await request.json()

    print(data)

    try:

        entry = data["entry"][0]
        changes = entry["changes"][0]
        value = changes["value"]

        message = value["messages"][0]["text"]["body"].lower()
        phone = value["messages"][0]["from"]

        response = RESPONSES.get(
            message,
            "Todavía no entiendo ese mensaje."
        )

        send_message(phone, response)

    except Exception as error:

        print("Error:", error)

    return {
        "status": "ok"
    }