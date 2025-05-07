


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