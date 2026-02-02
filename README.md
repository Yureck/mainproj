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

## Запуск тестов

```bash
python -m pytest tests/
```

## Лицензия

MIT
