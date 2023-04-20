"""
Создание сопрограммы при помощи asyncio
"""

import asyncio
async def my_coroutine() -> None:
    print('Hello world!')

result = asyncio.run(my_coroutine())
print(result)