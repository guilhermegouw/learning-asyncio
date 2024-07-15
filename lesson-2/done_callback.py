import asyncio


def handle(task):
    print(f"Task callback done: {task.done()}")


async def task_coroutine():
    print("Executing task_coroutine")
    await asyncio.sleep(1)


async def main():
    print("main coroutine")
    task = asyncio.create_task(task_coroutine())
    task.add_done_callback(handle)
    await task


asyncio.run(main())
