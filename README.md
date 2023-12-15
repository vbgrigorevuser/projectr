# Кейс с сетью ресторанов

## Инфомация для развертывания проекта (подразумевается, что у вас установлен Linux-дистрибутив)
1. Создание виртуального окружения ```python3 -m venv .venv```
2. Активация окружения ```source .venv/bin/activate```
3. Установка django ```pip install django```
4. Клонирование репозитория ```git clone git@github.com:vbgrigorevuser/projectr.git```
6. Переход в папку проекта ```cd projectr```
7. Запуск сервера по адресу ```http://127.0.0.1:8000/```
8. Открыть этот сайт в браузере (profit)

## Документация в деталях по созданию проекта
1. Создание django-проекта ```django-admin startproject projectr```
2. Создание django-приложения по аутентификации менеджеров ```python3 manage.py startapp managerauth```
3. Регистрация django-приложения в settings.py
4. Миграция стандартных моделей ```python3 manage.py makemigrations```, ```python3 manage.py migrate```
5. Создание суперпользователя ```python3 manage.py createsuperuser```
6. Проверка сервера ```python3 manage.py runserver``` 
7. Создание модели Manager (см. файл managerauth/models.py), миграции ```python3 manage.py makemigrations```, ```python3 manage.py migrate``` и регистрация на admin-сайте (managerauth/admin.py)
8. Создание урлов, и настройка вьюшки-заглушки (projectr/urls.py, managerauth/urls.py, managerauth/views.py)