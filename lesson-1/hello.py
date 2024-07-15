import asyncio


async def custom_coroutine():
    print("Hello, World!")


hello = custom_coroutine()
asyncio.run(hello)
