"""
Демонстрация различных типов функций в Python:
- Обычные функции с аннотациями типов
- Функции с global переменными
- Статические переменные функций
- Вложенные функции с nonlocal
"""

# ========== ПРОСТЫЕ ФУНКЦИИ ==========

def hello(name: str = "World") -> str:
    """Возвращает приветственное сообщение.
    
    Args:
        name: Имя для приветствия (по умолчанию "World")
    
    Returns:
        Строка с приветствием
    """
    return f"Hello, {name}!"

hello.__doc__ = "Return a greeting message."
print(hello())

def hello1(name):
    """Простое приветствие с проверкой имени.
    
    Args:
        name: Имя для приветствия (может быть False или пусто)
    """
    if not name:
        return  # Выходим если имя не передано
    print('Hello,' + name + '!')

hello1(False)  # Ничего не выведет
hello1("Alice")  # Output: Hello,Alice!


# ========== GLOBAL ПЕРЕМЕННЫЕ ==========
# global - это переменная вне функции, которая может быть изменена внутри функции

age = 30  # Глобальная переменная

def gggg():
    """Функция, которая изменяет глобальную переменную age."""
    global age  # Указываем, что используем глобальную переменную age
    age += 1
    print("Inside gggg(), age is:", age)

gggg()  # Output: Inside gggg(), age is: 31
print("Outside gggg(), age is:", age)  # Output: Outside gggg(), age is: 31


# ========== СТАТИЧЕСКИЕ ПЕРЕМЕННЫЕ ==========
# Статические переменные - это переменные, которые сохраняют значение между вызовами функции
# В Python это можно реализовать через атрибуты функции

def count():
    """Функция со статической переменной для подсчета вызовов.
    
    Returns:
        Количество вызовов функции
    """
    if not hasattr(count, "calls"):
        count.calls = 0  # Инициализируем статическую переменную при первом вызове
    count.calls += 1  # Увеличиваем счетчик
    return count.calls

# count() → 1
# count() → 2
# count() → 3


# ========== NONLOCAL И ВЛОЖЕННЫЕ ФУНКЦИИ ==========
# nonlocal - используется во вложенных функциях для изменения переменной из внешней функции

def count1():
    """Функция с вложенной функцией, использующей nonlocal.
    
    Демонстрирует печать значения через вложенную функцию.
    """
    count = 0  # Локальная переменная для count1

    def increment():
        """Вложенная функция, которая изменяет переменную count из внешней функции."""
        nonlocal count  # Указываем, что используем count из внешней функции
        count += 1
        print(count)
    
    increment()  # Output: 1


# ========== ВЛОЖЕННЫЕ ФУНКЦИИ С ВОЗВРАЩАЕМЫМ ЗНАЧЕНИЕМ ==========

def counter():
    """Возвращает функцию-инкрементор, которая увеличивает счетчик.
    
    Returns:
        Функция increment, которая увеличивает счетчик и возвращает его значение
    """
    count = 0  # Локальная переменная для counter

    def increment():
        """Вложенная функция, которая увеличивает и возвращает count."""
        nonlocal count
        count += 1
        return count
    
    return increment

# Использование:
# my_counter = counter()
# my_counter() → 1
# my_counter() → 2
# my_counter() → 3
    
    return increment

increment = counter()

print(increment())  # Output: 1
print(increment())  # Output: 2 
print(increment())  # Output: 3

