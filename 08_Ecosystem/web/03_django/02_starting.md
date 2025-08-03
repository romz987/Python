# Начало работы с Django

Установка:  

    pip install django 
    pythom -m django --version



Создаем новый проект Django:  

    django-admin startproject config .   // это очень хорошая практика 



Прикрутить postgres:

    1. устанавливаем psycopg2
    2. редактируем settings.py

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'educational_1',
            'USER': 'postgres',
            'PASSWORD': '12345678pass',
            'HOST': '194.190.152.45',
            'PORT': '5434'
        }
    }

    3. делаем миграцию: python manage.py migrate
    Мы создаем служебные таблицы, необходимые для работы Django, такие как таблицы для управления пользователями, сессиями и другими встроенными функциями, независимо от конкретного проекта.   
    Это обеспечивает корректную работу фреймворка.
