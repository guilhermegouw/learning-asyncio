import asyncio


async def task_coroutine():
    print("Executing task_coroutine")
    await asyncio.sleep(1)


async def main():
    print("main coroutine")
    task = asyncio.create_task(task_coroutine())
    await asyncio.sleep(0.5)
    was_cancelled = task.cancel()
    print(f"Task was cancelled: {was_cancelled}")
    await asyncio.sleep(0.1)
    print(f"Canceled: {task.cancelled()}")


asyncio.run(main())
