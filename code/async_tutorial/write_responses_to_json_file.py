import asyncio
import json
from types import resolve_bases

import aiohttp


URIS = (
    "https://api.github.com/orgs/python",
    "https://api.github.com/orgs/django",
    "https://api.github.com/orgs/pallets",
)


def write_to_file(data):
    with open("repo_data.json", "w") as json_file:
        json.dump(data, json_file)


async def fetch(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return {"naem": data["name"], "avatar_url": data["avatar_url"]}


async def main():
    async with aiohttp.ClientSession() as session:
        data = await asyncio.gather(*[fetch(session, url) for url in URIS])
        write_to_file(data)


asyncio.run(main())
