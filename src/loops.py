"""
Демонстрация циклов в Python:
- while цикл - повторяется пока условие True
- for цикл - повторяется для каждого элемента
- enumerate() - получить индекс и значение одновременно
"""

# ========== WHILE ЦИКЛ ==========
# while условие: - повторяет блок кода пока условие истинно (True)
# ВНИМАНИЕ: нужно изменять переменную в цикле, иначе бесконечный цикл!

counter = 0  # Инициализируем счетчик
while counter < 10:
    print("Counter is at:", counter)
    counter += 1  # Увеличиваем счетчик каждую итерацию


# ========== FOR ЦИКЛ С RANGE ==========
# for переменная in range(n): - повторяет цикл n раз (от 0 до n-1)
# range(5) генерирует: 0, 1, 2, 3, 4

for i in range(5):
    print("Iteration:", i)


# ========== FOR ЦИКЛ ПО ЭЛЕМЕНТАМ ==========
# for элемент in список: - повторяется для каждого элемента в списке

items = ['apple', 'banana', 'cherry']
for item in items:
    print("Item:", item)


# ========== ENUMERATE() - ИНДЕКС И ЗНАЧЕНИЕ ==========
# enumerate(список) - возвращает пары (индекс, элемент)
# Полезно когда нужны и индекс, и значение элемента

for index, value in enumerate(items):
    print(f"Index: {index}, Value: {value}")

# Output:
# Index: 0, Value: apple
# Index: 1, Value: banana
# Index: 2, Value: cherry