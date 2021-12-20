"""
This example is from Linkedin learning, the following is article URL where I found this code
https://www.linkedin.com/learning/async-python-foundations-applied-concepts/chat-app-using-quart
"""

import asyncio
import json

from quart import Quart, websocket, render_template

from redis_db import ChatDB


app = Quart(__name__)

connections = set()

chat_db = ChatDB("chat_room")


@app.before_serving
async def init_db():
    await chat_db.start_db()


@app.websocket("/ws")
async def ws():
    connections.add(websocket._get_current_object())
    try:
        while True:
            message = await websocket.receive()
            await chat_db.save_message(json.loads(message))
            send_coroutines = [connection.send(message) for connection in connections]
            await asyncio.gather(*send_coroutines)
    finally:
        connections.remove(websocket._get_current_object())


@app.route("/")
async def chat():
    messages = await chat_db.get_messages()
    return await render_template("chat_redis.html", messages=messages)


app.run(use_reloader=True, port=3000, debug=True)
