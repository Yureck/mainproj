"""
Обработка исключений (Exception Handling) в Python

Исключение — это событие, которое происходит во время выполнения программы и нарушает
её нормальный ход. Python предоставляет механизм для перехвата и обработки ошибок.

Структура try-except-else-finally:
- try: блок кода, который может вызвать исключение
- except ИсключениеType: блок кода для обработки конкретного типа исключения
- else: выполняется ТОЛЬКО если в try не было исключений
- finally: выполняется ВСЕГДА, независимо от того, было ли исключение или нет

Типичные встроенные исключения:
- Exception: базовый класс для всех исключений
- ZeroDivisionError: деление на ноль
- FileNotFoundError: файл не найден
- ValueError: неправильный тип значения
- TypeError: неправильный тип данных
- KeyError: ключ не найден в словаре
- IndexError: индекс вне границ списка

Кастомные исключения создаются путём наследования от Exception.

Пример базовой структуры try-except:
"""

try:
	pass
except Exception:
	pass
else:
    pass
finally:
    pass

# ========== ПРИМЕР 1: Деление на ноль ==========
# ZeroDivisionError возникает при попытке деления на ноль
# finally гарантирует, что код выполнится в любом случае

try:
	result = 2 / 0
	print(result)
except ZeroDivisionError:
	print("Ошибка: деление на ноль!")
finally:
	result = 1
print(result)  # Output: 1


# ========== ПРИМЕР 2: Явный raise исключения ==========
# raise Exception() — это способ самостоятельно выбросить (вызвать) исключение
# Полезно для проверки условий и создания собственной логики обработки ошибок

try:
    raise Exception("Это пример вызова исключения")
except Exception as error:
    print(f"Поймано исключение: {error}")  # Output: Поймано исключение: Это пример вызова исключения


# ========== ПРИМЕР 3: Кастомное исключение ==========
# Можно создавать свои типы исключений, наследуя от Exception
# Это полезно для специфичных ошибок в вашем приложении

class CustomError(Exception):
    """Пользовательское исключение для демонстрации."""
    pass

try:
    raise CustomError("Это пользовательская ошибка!")
except CustomError as custError:
    print(f"Поймано пользовательское исключение: {custError}")  # Output: Поймано пользовательское исключение: Это пользовательская ошибка!


# ========== ПРИМЕР 4: FileNotFoundError ==========
# FileNotFoundError возникает при попытке открыть несуществующий файл
# Использование finally гарантирует, что файл будет закрыт даже при ошибке

try:
      file = open("non_existent_file.txt", "r")
      content = file.read() 
      print(content)
except FileNotFoundError as fnf_error:
      print(f"Ошибка: Файл не найден! {fnf_error}") 
finally:
      try:
          file.close()
      except NameError:
          pass


# ========== ПРИМЕР 5: Context manager (with statement) ==========
# with автоматически управляет ресурсами (открытие/закрытие файлов)
# Это более надёжный способ работы с файлами, чем try-finally
# Файл автоматически закроется, даже если произойдёт ошибка

with open("non_existent_file.txt", "r") as file:
    content = file.read()
