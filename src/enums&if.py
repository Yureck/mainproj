"""
Демонстрация типов данных, условных операторов и Enum.

Включает:
- Проверка типов (type, isinstance)
- Условный оператор if-else и тернарный оператор
- Комплексные числа (Complex)
- Enum класс для перечислений
"""

# ========== ПРОВЕРКА ТИПОВ ==========

name = "beau"
__name__ = "main"
name1 = "beau"

# type() - возвращает тип переменной
print(type(name))  # Output: <class 'str'>

# isinstance(переменная, тип) - проверяет, является ли переменная этого типа
print(isinstance(name1, str))  # Output: True


# ========== ТИПЫ ДАННЫХ: FLOAT ==========

age = float(25)
print(isinstance(age, float))  # Output: True

# Переопределяем age как int
age = 8
age += 2
print(age)  # Output: 10

age = 2
print(age)  # Output: 2


# ========== УСЛОВНЫЕ ОПЕРАТОРЫ ==========

def is_adult(age):
    """Проверяет, является ли человек взрослым (18+)."""
    if age >= 18:
        return True
    else:
        return False

def is_adult2(age):
    """Компактная версия: возвращает True если 18+."""
    return age >= 18

print(is_adult2(20))  # Output: True

# Тернарный оператор: условие ? значение_если_true : значение_если_false
# Синтаксис Python: значение_если_true if условие else значение_если_false
def is_adult3(age):
    """Версия с тернарным оператором."""
    return True if age >= 18 else False


# ========== КОМПЛЕКСНЫЕ ЧИСЛА ==========
# Комплексные числа: a + bi, где i - мнимая единица

num1 = 2 + 3j  # Способ 1: литерал
num2 = complex(2, 3)  # Способ 2: конструктор complex()

# .real - вещественная часть
# .imag - мнимая часть
print(num2.real, num2.imag)  # Output: 2.0 3.0


# ========== ENUM - ПЕРЕЧИСЛЕНИЯ ==========
# Enum используется для создания набора констант (перечисления)

from enum import Enum

class State(Enum):
    """Перечисление состояний задачи."""
    NEW = 1  # Новое
    IN_PROGRESS = 2  # В процессе
    COMPLETED = 3  # Завершено

# Доступ к элементу enum
print(State.NEW)  # Output: State.NEW

# .name - имя элемента
print(State.NEW.name)  # Output: NEW

# .value - значение элемента
print(State.NEW.value)  # Output: 1

# Получение по значению
print(State(1).value)  # Output: 1

# Получение по имени
print(State['NEW'].name)  # Output: NEW  
