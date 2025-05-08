
# Spravochnik API

## Описание
API для справочника организаций, построенный на FastAPI. Реализована базовая структура проекта с подключением SQLite, миграциями через Alembic и базовым CRUD для сущности `Organization`.

## Реализовано
- Настройка FastAPI с базовым эндпоинтом (`/`).
- Подключение SQLite через SQLAlchemy.
- Миграции базы данных с помощью Alembic.
- Модель и CRUD-операции для сущности `Organization`.
- Базовые эндпоинты для создания организаций (`POST /organizations/`).

## Установка
1. Клонируйте репозиторий: `git clone https://github.com/meloch287/Spravochnik.git`
2. Установите зависимости: `pip install -r requirements.txt`
3. Запустите миграции: `alembic upgrade head`
4. Запустите сервер: `uvicorn app.main:app --reload`

## Текущий статус
Проект находится в стадии разработки. Далее планируется добавление остальных моделей (`Building`, `Activity`, `City`), фильтрации по координатам и тестов.

```
Spravochnik
├── alembic/                      # Миграции базы данных
├── app/
│   ├── __init__.py
│   ├── main.py                   # Точка входа FastAPI
│   ├── core/
│   │   ├── config.py            # Настройки (например, через pydantic.BaseSettings)
│   ├── db/
│   │   ├── base.py              # Базовые модели для импорта
│   │   ├── session.py           # Создание сессий SQLAlchemy
│   │   └── init_db.py          # Скрипт инициализации с тестовыми данными
│   ├── models/
│   │   ├── organization.py
│   │   ├── building.py
│   │   ├── activity.py
│   │   └── city.py
│   ├── schemas/
│   │   ├── organization.py
│   │   ├── building.py
│   │   ├── activity.py
│   │   └── city.py
│   ├── crud/
│   │   ├── organization.py
│   │   ├── building.py
│   │   ├── activity.py
│   │   └── city.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py              # Зависимости (например, получение БД-сессии)
│   │   ├── v1/
│   │   │   ├── api.py           # Подключение роутов
│   │   │   ├── organization.py
│   │   │   ├── building.py
│   │   │   ├── activity.py
│   │   │   └── city.py
│   └── utils/
│       └── geo.py              # Утилиты для фильтрации по координатам
├── tests/
│   ├── test_organization.py
│   ├── test_building.py
│   ├── test_activity.py
│   └── test_city.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```
