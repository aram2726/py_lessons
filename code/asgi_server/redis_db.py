
"""
This example is from Linkedin learning, the following is article URL where I found this code
https://www.linkedin.com/learning/async-python-foundations-applied-concepts/chat-app-using-quart
"""

import json

import aioredis


class ChatDB:

    def __init__(self, room_name):
        self.room_name = room_name
        self.redis = None

    async def start_db(self):
        self.redis = aioredis.from_url("redis://localhost")
        await self.redis.set("room_name", self.room_name)

    async def save_message(self, message_dictionary):
        room_name = await self.redis.get("room_name")
        message_json = json.dumps(message_dictionary)
        await self.redis.rpush(room_name, message_json)

    async def clear_db(self):
        await self.redis.flushall()

    async def get_messages(self):
        room_name = await self.redis.get("room_name")
        messages_json = await self.redis.lrange(room_name, 0, -1)
        messages = []
        for message in messages_json:
            message_dict = json.loads(message)
            messages.append(message_dict)
        return messages
