# Серверная инфрастуктура

- [Glossary](#glossary)
- [WSGI и ASGI](#wsgi-%D0%B8-asgi)
- [How it works](#how-it-works)
- [Источники](#%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8)

______________________________________________________________________

## Glossary

Спецификация - технический документ с детальным описанием объекта спецификации, перечислением его специфических особенностей и детальным перечислением условий, которым должен соотвествовать объект.

______________________________________________________________________

## WSGI и ASGI

**WSGI** и **ASGI** это спецификация стандартного интерфейса между web server и python application.
В соотвествии с этой спецификации реализуется **application server**, задачей которого является осуществление взаимодействия между **web server** и **python application**.

### **WSGI (Web Server Gateway Interface)**

> [!NOTE]
> Описан в PEP333

- Создан в 2003 году для простых HTTP-запросов (request → response)
- Предполагает синхронную модель исполнения — один поток/процесс обрабатывает один запрос
- Не поддерживает WebSocket или “живые” соединения
- Подходит для классических приложений: HTML-страницы, REST-API и т.п

### **ASGI (Asynchronous Server Gateway Interface)**

> [!NOTE]
> Описан в ASGI Documentation

- Продукт эволюции WSGI, созданный для Python-асинхронности (async/await)
- Позволяет одному процессу работать с множеством одновременных запросов
- Поддерживает помимо HTTP ещё и долгоживущие соединения: WebSockets, SSE, gRPC
- Полезен для realtime-приложений (чатов, игр, уведомлений)

______________________________________________________________________

## How it works

Web server (Apache, Nginx, Caddy) -> Application server (uWSGI, Gunicorn) -> Python Application (Flask, Quart, Django, FastAPI)

______________________________________________________________________

## Источники

[PEP 333 – Python Web Server Gateway Interface](https://peps.python.org/pep-0333/)
[ASGI Documentation](https://asgi.readthedocs.io/en/latest/)
