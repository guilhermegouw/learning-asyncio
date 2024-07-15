import asyncio


async def task_coroutine():
    print("Executing task_coroutine")
    await asyncio.sleep(1)


async def main():
    print("main coroutine")
    task = asyncio.create_task(task_coroutine())
    await task


asyncio.run(main())
