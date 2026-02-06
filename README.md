# Python Project Template

Пустой проект-шаблон для тестов и обучения по Python.

## Структура проекта

```
.
├── src/                 # Исходный код проекта
├── tests/              # Тесты
├── README.md           # Этот файл
├── requirements.txt    # Зависимости проекта
└── .gitignore         # Исключения для Git
```

## Установка

1. Создайте виртуальное окружение:
```bash
python -m venv venv
```

2. Активируйте виртуальное окружение:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

# mainproj — Python learning & test template

Это компактный шаблон-проект на Python для обучения базовым концепциям и
практики с тестированием. Проект содержит небольшие иллюстративные модули в
папке `src/` (списки, словари, кортежи, множества, функции, классы, декораторы,
исключения, list-comprehensions, map/filter/reduce, и т.п.) и примеры тестов в
`tests/`.

Цель: дать готовую площадку для экспериментов и написания небольших упражнений
и юнит-тестов.

---

## Структура проекта

```
.
├── src/                 # Примеры и учебные модули (lists, dicts, functions...)
├── tests/               # Примеры pytest тестов
├── README.md            # Этот файл
├── requirements.txt     # Зависимости для тестов/бенчмарков
└── .gitignore           # Исключения Git
```

## Что в `src/`

- `listcomp.py` — примеры list comprehensions и микробенчмарки сравнения с map/filter/loop.
- `decorators.py` — объяснение декораторов и пример `logtime`.
- `exeptions.py` — примеры try/except/else/finally, кастомные исключения и work-with-files.
- `lambdafunc.py` — lambda-функции, `map`, `filter`, `reduce` с пояснениями.
- `functions.py` — разные формы функций, `global`, `nonlocal`, статические атрибуты.
- `lists.py`, `dictionaries.py`, `tuples.py`, `sets.py` — базовые операции со структурами данных.
- `classess.py`, `object.py`, `dog.py` — классы и наследование, примеры OOP.
- `main.py` — пример использования `argparse` (CLI).
- `recursion.py` — (если есть) примеры рекурсии и связанных задач.

Откройте любой модуль в `src/` — он содержит поясняющие комментарии и небольшие
примеры запуска.

## Установка и запуск

Рекомендуется создавать виртуальное окружение и устанавливать зависимости:

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

macOS / Linux (bash/zsh):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Быстрый старт — примеры и тесты

- Запустить примеры (например list-comprehensions и бенчмарки):

```powershell
python src\listcomp.py
```

- Запустить демонстрацию декоратора:

```powershell
python src\decorators.py
```

- Запустить тесты (pytest):

```powershell
python -m pytest -q
```

## Производительность и бенчмарки

В `src/listcomp.py` есть простой микробенчмарк на `timeit`, который сравнивает
list-comprehension, `map+lambda` и обычный цикл `for` для трансформаций и
фильтрации. Результаты зависят от Python-версии и платформы — используйте их
как ориентир.

## Внесение изменений

- Добавьте новые примеры в `src/` и соответствующие тесты в `tests/`.
- Для новых зависимостей редактируйте `requirements.txt`.

## Предложения и след. шаги

- Можно добавить `pyproject.toml` и настроить линтер/formatter (`black`, `ruff`).
- Автоматизировать CI (GitHub Actions) для запуска тестов и бенчмарков при
	пуше в репозиторий.

---

Если хотите, могу:
- добавить секцию «Как добавить упражнение»,
- подготовить шаблон теста `pytest` для новых модулей,
- или настроить простой GitHub Actions workflow для запуска тестов.

