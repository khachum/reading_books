"""
Создаем сопрограмму и смотрим, что выведет непосредственный ее вызов
"""


async def coroutine_add_one(number: int) -> int:
    return number + 1


def add_one(number: int) -> int:
    return number + 1

# Здесь реально выполняется работа
function_result = add_one(1)
# Данная сопрограмма не запустится, а переменная
# coroutine_result будет иметь тип <class 'coroutine'>
coroutine_result = coroutine_add_one(1)

print(f'Function result is {function_result} and the type is {type(function_result)}')
print(f'Coroutine result is {coroutine_result} and the type is {type(coroutine_result)}')