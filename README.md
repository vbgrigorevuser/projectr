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
```
INSTALLED_APPS = [
    'managerauth.apps.ManagerauthConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```