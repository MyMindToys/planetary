# Planetary

Django-проект: бэкенд и админка на Django, фронт — Vue.

## Структура

```
planetary/
├── manage.py
├── requirements.txt
├── planetary/           # настройки проекта
├── content/             # приложение: контент и изображения (админка)
├── templates/           # шаблоны бэкенда и админки
│   ├── base.html
│   ├── content/
│   └── admin/
├── static/              # статика Django (css, js, img)
├── media/               # загруженные файлы (изображения)
├── frontend/            # проект на Vue (пока пусто)
├── ks/                  # скрипты и служебное (не часть приложения)
└── db.sqlite3           # БД (после migrate)
```

## Установка и запуск

```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # для входа в админку
python manage.py runserver
```

- Сайт: http://127.0.0.1:8000/
- Админка: http://127.0.0.1:8000/admin/

Изображения добавляются через админку (модель «Изображения» в приложении content).
