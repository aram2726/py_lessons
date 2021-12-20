import asyncio


def sync_wraper(func):
    async def wraper():
        await asyncio.sleep(1)
        print("decorator worked")
        await func()
    return wraper


def bar(param1):
    print('bar has been called')
    def inner(func):
        print('inner has been called')
        async def baz():
            print(param1)
            print('baz has been called')
            await func()
        return baz
    return inner


@sync_wraper
async def async_func():
    await asyncio.sleep(1)
    print("async_func is called")

@bar(1, 2)
async def async_func_two():
    await asyncio.sleep(1)
    print("async_func_two is called")



async def main():
    print("Staring functions call")
    await asyncio.gather(
        async_func(),
        async_func_two(),
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
