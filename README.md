## Структура проекта
```
cat_charity_fund:
    ├── alembic
    │   ├── README
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions
    ├── app
    │   ├── __init__.py
    │   ├── api
    │   │   ├── endpoints
    │   │   │   └──...
    │   │   └── ...
    │   ├── core
    │   │   └── ...
    │   ├── crud
    │   │   └── ...
    │   ├── main.py
    │   ├── models
    │   │   └── ...
    │   ├── schemas
    │   │   └── ...
    │   └── services
    │       └── ...
    ├── tests
    │   └── ...
    ├── venv
    │   └── ...
    ├── .flake8
    ├── .gitignore
    ├── alembic.ini
    ├── openapi.json
    ├── pytest.ini
    ├── README.md
    └── requirements.txt
```

## Запуск проекта
1. Клонировать репозиторий:
```bash
git clone https://github.com/vovanbart/cat_charity_fund.git
```

2. Создать и активировать виртуальное окружение:
```bash
python3 -m venv venv
bash/zsh
source venv/bin/activate
Windows:
venv\Scripts\activate.bat
```

3. Обновить pip и установить зависимости из ```requirements.txt```
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Создать и заполнить файл **.env**:

```bash
touch .env
```

5. Выполнить миграции:
```bash
alembic upgrade head
```

6. Запустить проект:
```bash
uvicorn app.main:app
```

После запуска проект будет доступен по адресу: http://127.0.0.1:8000

Документация к API досупна по адресам:
- Swagger: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc