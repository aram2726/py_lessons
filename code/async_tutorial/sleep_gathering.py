import asyncio


async def sleep_five():
    print("Sleeping 5 seconds...")
    await asyncio.sleep(5)
    print("Woke up from 5 seconds!")


async def sleep_three_than_five():
    print("Sleeping 3 seconds...")
    await asyncio.sleep(3)
    await sleep_five()
    print("Woke up from 3 + 5 seconds!")



async def main():
    await asyncio.gather(
        sleep_five(),
        sleep_three_than_five()
    )


asyncio.run(main())
