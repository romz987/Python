# Состав 


Django - это пакет со вложенными модулями и классами.  


1. django.db  

    db модуль
    Содержит классы, функции и подмодули, связанные с базой данных. 




2. django.contrib 

    contrib модуль  
    Содержит набор встроенных переиспользуемых приложений, которые можно подключать к своему проекту.

    auth         - аутентификация и управление пользователями (User, Group, Permission)
    admin        - административный интерфейс
    sessions     - поддержка сессий  
    messages     - система сообщений (флеш-сообщения)
    staticfiles  - управление статическими файлами
    contenttypes - слежение за типами моделей
    sites        - поддержка мультисайтовости  
    humanize     - человеко-понятный формат вывода чисел, дат и т.д.  
    sitemaps     - генерация xml sitemap  
    flatpages    - простые статические страницы через админку  
    redirects    - управление редиректами через бд


3. django.urls 

    urls модуль
    Маршрутизация 



4. django.http  

    работа с запросами ответами



5. django.shortcuts

    удобные функции для view 



6. django.forms

    работа с формами



7. django.views 

    CBV представления



8. django.middleware  

    Базовый класс MiddlewareMixin, плюс встроенные middleware (например, AuthenticationMiddleware).



9. django.core 

    management - команды управления  
    validators, exceptions, mail, files и др



10. django.conf 

    setting -доступ к настройкам проекта
