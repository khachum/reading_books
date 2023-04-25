"""Первое применение sleep"""

import asyncio

async def hello_world_message() -> str:
    # asyncio.sleep() -- сопрограмма, поэтому вызываем при помощи await
    await asyncio.sleep(1)
    return 'Hello World!'

async def main() -> None:
    message = await hello_world_message()
    print(message)

asyncio.run(main())