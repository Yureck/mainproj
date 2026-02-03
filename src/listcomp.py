"""
List Comprehensions (Сжатие списков) в Python

List Comprehension — это компактный способ создания нового списка путём применения
операции к каждому элементу существующего списка, часто с фильтрацией.

Синтаксис:
    [выражение for элемент in итерируемый_объект if условие]

Преимущества:
- Более читаемый и компактный код чем циклы for
- Быстрее, чем обычные циклы
- Более "pythonic" (идиоматичный) способ

Сравнение с традиционным циклом:
    # Традиционный способ:
    squared = []
    for x in numbers:
        squared.append(x ** 2)
    
    # List comprehension (компактнее):
    squared = [x ** 2 for x in numbers]
    
    # С фильтром (условием):
    squared = [x ** 2 for x in numbers if x % 2 == 0]

Примеры ниже показывают различные способы фильтрации и трансформации списков.
"""

numbers = [1, 2, 3, 4, 5]


# ========== ПРИМЕР 1: List comprehension с фильтром ==========
# Оставляем только чётные числа (x % 2 == 0 означает остаток от деления на 2 равен 0)
numbers_even = [x for x in numbers if x % 2 == 0]
print(numbers_even)  # Output: [2, 4]   


# ========== ПРИМЕР 2: Традиционный способ vs List comprehension ==========
# Способ 1: Традиционный цикл for (многострочный, более подробный)
numb_pow_2 = []
for x in numbers:
    numb_pow_2.append(x ** 2)

# Способ 2: List comprehension (компактный, более читаемый)
# Возводит каждый элемент в квадрат (x ** 2)
numbers_powered = [x ** 2 for x in numbers]
print(numbers_powered)  # Output: [1, 4, 9, 16, 25]

# Способ 3: Использование map() с lambda функцией (функциональный стиль)
# Это более функциональный подход, но менее читаемый чем list comprehension
numb_pow_3 = list(map(lambda x: x ** 2, numbers))
print(numb_pow_3)  # Output: [1, 4, 9, 16, 25]


# Вывод: List comprehension (Способ 2) обычно предпочтительнее по читаемости


# ========== СРАВНЕНИЕ: comprehension vs map/filter/reduce ==========
# Краткая сводка:
# - List comprehension: компактно, читабельно, "pythonic" для большинства задач.
# - map/filter: могут быть ленивыми (в Python 3 возвращают итератор) — экономят память.
#   Удобны, когда есть готовая именованная функция. Комбинирование map/filter с lambda
#   иногда ухудшает читаемость.
# - reduce: используется для сведения последовательности к одному значению. Часто
#   его заменяют на встроенные функции (`sum`, `any`, `all`, `min`, `max`) или на
#   явный цикл для лучшей читаемости.
#
# Примеры эквивалентов:
# Фильтрация чётных чисел
#   comprehension:
#       [x for x in numbers if x % 2 == 0]
#   filter (лениво):
#       list(filter(lambda x: x % 2 == 0, numbers))
#
# Трансформация (возвести в квадрат)
#   comprehension:
#       [x**2 for x in numbers]
#   map (лениво):
#       list(map(lambda x: x**2, numbers))
#
# Свёртка (reduce) vs sum
#   reduce:
#       reduce(lambda acc, x: acc + x, numbers, 0)
#   предпочтительнее sum:
#       sum(numbers)


# ========== БЕНЧМАРК: небольшой тест производительности ==========
# Добавлены вспомогательные функции и простой runner, который запускается
# при запуске модуля напрямую. Это поможет видеть относительную разницу в
# типичных примерах. (Не использует очень большие наборы данных по умолчанию.)

def comp_squares(nums):
    return [x ** 2 for x in nums]


def map_squares(nums):
    return list(map(lambda x: x ** 2, nums))


def loop_squares(nums):
    out = []
    for x in nums:
        out.append(x ** 2)
    return out


def comp_filter(nums):
    return [x for x in nums if x % 2 == 0]


def filter_func(nums):
    return list(filter(lambda x: x % 2 == 0, nums))


def run_bench():
    import timeit
    N = 10000
    numbers_bench = list(range(N))
    repeats = 100

    print("\nRunning quick benchmarks (this may take a few seconds)...")

    # Используем callable-версии timeit, чтобы локальные переменные были корректно захвачены
    t_comp = timeit.timeit(lambda: comp_squares(numbers_bench), number=repeats)
    t_map = timeit.timeit(lambda: map_squares(numbers_bench), number=repeats)
    t_loop = timeit.timeit(lambda: loop_squares(numbers_bench), number=repeats)

    print(f"Squares: comprehension: {t_comp:.4f}s, map+lambda: {t_map:.4f}s, loop+append: {t_loop:.4f}s (N={N}, repeats={repeats})")

    t_comp_f = timeit.timeit(lambda: comp_filter(numbers_bench), number=repeats)
    t_filter = timeit.timeit(lambda: filter_func(numbers_bench), number=repeats)
    print(f"Filter evens: comprehension: {t_comp_f:.4f}s, filter+lambda: {t_filter:.4f}s (N={N}, repeats={repeats})")


if __name__ == '__main__':
    # Запуск примеров и бенчмарка для быстрой проверки
    print('\n--- Running examples and micro-benchmarks from listcomp.py ---')
    print('numbers:', numbers[:10])
    print('Even numbers (comprehension):', numbers_even)
    print('Powered (comprehension):', numbers_powered[:10])
    run_bench()

