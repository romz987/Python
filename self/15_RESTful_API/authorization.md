# АВТОРИЗАЦИЯ

Стандарт OAuth2


1. Basic Authentication

Отправляется в заголовке Authorization

Формат: Authorization: Basic base64(username:password)

Пример: Authorization: Basic YWRtaW46cGFzc3dvcmQ=

Плюсы: просто
Минусы: небезопасно без HTTPS, пароль передаётся (хоть и закодирован)
Когда использовать: только с HTTPS и в защищённых внутренних сервисах


2. Digest Authentication

Сервер шлёт клиенту challenge (nonce)  

Клиент отвечает хэшем (обычно MD5), включающим пароль, nonce и метод

Пример:

Authorization: Digest username="admin", realm="example", nonce="...", uri="/", response="..."

Плюсы: пароль не передаётся
Минусы: сложнее в реализации, редко используется

Когда использовать: почти никогда сейчас — устарело, заменено токенами



3. Token Authentication / Bearer
Отправляется токен (API-ключ, JWT и т.д.) в заголовке Authorization

Формат: Authorization: Bearer <token> 

Плюсы:

    Безопасно при правильной реализации

    Гибко (можно использовать JWT, OAuth и т.д.)

    Совместимо с большинством API и библиотек

Когда использовать: почти всегда при разработке современных API
