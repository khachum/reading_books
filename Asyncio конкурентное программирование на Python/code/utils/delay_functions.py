import asyncio

async def delay(seconds: int) -> int:
    print(f'sleep for {seconds} second(s)')
    await asyncio.sleep(seconds)
    print(f'finished sleeping for {seconds} second(s)')
    return seconds