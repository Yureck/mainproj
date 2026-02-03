"""
Демонстрация работы с аргументами командной строки (sys.argv и argparse).
Файл показывает как обрабатывать входные параметры при запуске программы.
"""

import argparse
from email import parser
import sys

print("Hello from main.py!")

# sys.argv - это список всех аргументов переданных при запуске программы
# Первый элемент - это имя самого скрипта
print(sys.argv)  # Print command-line arguments
# Пример: python main.py arg1 arg2 → ['main.py', 'arg1', 'arg2']

# ========== ARGPARSE - удобный парсер для командной строки ==========
# argparse помогает создавать красивый интерфейс командной строки с помощью флагов
parser.argparse.ArgumentParser(description="A simple command-line tool.")

# Добавляем флаг --name (опциональный аргумент)
# type=str означает, что значение будет строкой
parser.add_argument("--name", type=str, help="Your name")

# Добавляем флаг --age (опциональный аргумент)
# type=int означает, что значение будет целым числом
parser.add_argument("--age", type=int, help="Your age") 

# Парсим аргументы и получаем объект с атрибутами
args = parser.parse_args()

# Проверяем, был ли передан флаг --name
if args.name:
    print(f"Hello, {args.name}!")

# Добавляем расширенный флаг --age с ограничениями (от 1 до 100)
parser.add_argument("--age", choices=[str(i) for i in range(1, 101)], help="Your age between 1 and 100")

# Проверяем, был ли передан флаг --age
if args.age:
    print(f"You are {args.age} years old!")

# Пример использования:
# python main.py --name "Юрий" --age 25
# Output: Hello, Юрий!
#         You are 25 years old!