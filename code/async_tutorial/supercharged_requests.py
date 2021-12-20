import asyncio

from datetime import datetime
from pprint import pprint

import aiohttp
import requests
import click

urls = [
    "http://httpbin.org/get?text=python",
    "http://httpbin.org/get?text=is",
    "http://httpbin.org/get?text=fun",
    "http://httpbin.org/get?text=and",
    "http://httpbin.org/get?text=useful",
    "http://httpbin.org/get?text=you",
    "http://httpbin.org/get?text=can",
    "http://httpbin.org/get?text=almost",
    "http://httpbin.org/get?text=do",
    "http://httpbin.org/get?text=anything",
    "http://httpbin.org/get?text=with",
    "http://httpbin.org/get?text=it",
]


def get_args(url):
    return requests.get(url).json()["args"]


async def fetch_args(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return data["args"]


start = datetime.now()
pprint([get_args(url) for url in urls])
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")


async def main():
    async with aiohttp.ClientSession() as session:
        fetch_coroutines = []
        for url in urls:
            fetch_coroutines.append(fetch_args(session, url))
        # No http requests have been sent untill this line.
        data = await asyncio.gather(*fetch_coroutines)
        pprint(data)

start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
