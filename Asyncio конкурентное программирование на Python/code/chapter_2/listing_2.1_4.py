"""
Используем ключевое слово await
"""

import asyncio

async def add_one(number: int) -> int:
    return number + 1


async def main() -> None:
    # Здесь программа приостанавливается и ждет выполнения сопрограммы add_one(1)
    one_plus_one = await add_one(1)

    # Здесь программа приостанавливается и ждет выполнения сопрограммы add_one(2)
    two_plus_one = await add_one(2)
    print(one_plus_one)
    print(two_plus_one)


asyncio.run(main())
