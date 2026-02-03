names = ("Alice", "Bob", "Charlie", "Diana")

# Получение последнего элемента по индексу
print(names[-1])  # Output: Diana

# Получение элемента по индексу
print(names[0])  # Output: Alice

# ВНИМАНИЕ! Кортежи неизменяемы - это вызовет ошибку:
# names[1] = "Eve"  # TypeError: 'tuple' object does not support item assignment

# index() - возвращает индекс первого найденного элемента
print(names.index("Charlie"))  # Output: 2

# count() - подсчитывает количество элементов с значением
print(names.count("Alice"))  # Output: 1

# Проверка наличия элемента (in)
print("Eve" in names)  # Output: False

# Слайсинг (срезы) - получить подкортеж
print(names[0:2])  # Output: ('Alice', 'Bob')

# sorted() - возвращает отсортированный СПИСОК (не кортеж!)
print(sorted(names))  # Output: ['Alice', 'Bob', 'Charlie', 'Diana']

# Конкатенация - объединение кортежей (создает новый кортеж)
newtuples = names + ("Eve", "Frank")
print(newtuples)  # Output: ('Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank')