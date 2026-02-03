"""
Демонстрация КЛАССОВ И НАСЛЕДОВАНИЯ в Python.

Основные концепции:
- Класс (Class) - это шаблон для создания объектов
- Метод __init__() - конструктор класса
- Наследование - подкласс наследует свойства и методы базового класса
- Переопределение методов (Override) - подкласс может переопределить методы базового класса
"""

# ========== БАЗОВЫЙ КЛАСС ==========

class Animal:
    """Базовый класс для всех животных."""
    
    def __init__(self, name, species):
        """Конструктор класса Animal.
        
        Args:
            name: Имя животного
            species: Вид животного
        """
        self.name = name
        self.species = species
    
    def make_sound(self):
        """Издает звук (базовая реализация).
        
        Returns:
            Описание звука
        """
        return "Some generic sound"


# ========== ПОДКЛАСС (НАСЛЕДОВАНИЕ) ==========

class Dog(Animal):
    """Класс Собака, наследует от класса Animal."""
    
    def __init__(self, name, age):
        """Конструктор класса Dog.
        
        Args:
            name: Имя собаки
            age: Возраст собаки
        """
        self.name = name
        self.age = age

    def bark(self):
        """Лай собаки.
        
        Returns:
            Звук лая
        """
        return "Woof!"

    def get_info(self):
        """Получить информацию о собаке.
        
        Returns:
            Строка с информацией о собаке
        """
        return f"{self.name} is {self.age} years old."


# ========== СОЗДАНИЕ ОБЪЕКТА И ВЫЗОВ МЕТОДОВ ==========

# Создаем объект класса Dog
roger = Dog("Roger", 4)
print(roger.bark())  # Output: Woof!
print(roger.get_info())  # Output: Roger is 4 years old.
