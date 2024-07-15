"""
For this example there will be a long task. 
    - This task will have a duration of 20 secs.
    - This will be the first task to start.
    - it will print "Starting long task" when it starts.
    - A done callback will be added to the task.
    - The callback will print "Long task done"
There will be a short task.
    - This task will have a duration of 1 sec.
    - This will be the second task to start.
    - It will be called multiple times.
        - Each time it will print "Starting short task for the {i} time... "
There will be a third task.
    - This task will have a middle duration of 10 secs.
    - This will be the third task to start.
    - It will be called twice.
      - First time it will print "Starting middle task"
        - It will be called again right after the first time.
        - The second time we need to check if the task was cancelled.
          if not cancelled, print "Middle task running"
        Then cancel the task.
        print "Middle task cancelled"
"""

import asyncio
import time


async def long_task():
    print("Starting long task")
    await asyncio.sleep(20)
    print("Long task completed")


def long_task_done(task):
    print("Long task done")


async def short_task(i):
    print(f"Starting short task for the {i} time... ")
    await asyncio.sleep(1)
    print(f"Short task {i} completed")


async def middle_task():
    print("Starting middle task")
    await asyncio.sleep(10)
    print("Middle task completed")


async def main():
    start_time = time.time()
    long_task_instance = asyncio.create_task(long_task())
    long_task_instance.add_done_callback(long_task_done)

    short_task_instance = [asyncio.create_task(short_task(i + 1)) for i in range(20)]
    middle_task_instance = asyncio.create_task(middle_task())

    await asyncio.sleep(5)
    second_middle_task_instance = asyncio.create_task(middle_task())
    await asyncio.sleep(5)

    if not middle_task_instance.cancelled():
        print("Middle task running")
    second_middle_task_instance.cancel()
    try:
        await second_middle_task_instance
    except asyncio.CancelledError:
        print("Middle task cancelled")

    await asyncio.gather(*short_task_instance)
    await long_task_instance
    finish = time.time()
    print(f"Time taken: {finish - start_time}")


asyncio.run(main())
