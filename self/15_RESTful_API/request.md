# ЗАПРОС (REQUEST)

## Содержание  

[Источники](#Источники)
[Передача данных в запросе](#Передача-данных-в-запросе)



----
## Источники 

[RFC7231 - official http specification](https://datatracker.ietf.org/doc/html/rfc7231)
[MDN - http lessons](https://developer.mozilla.org/en-US/docs/Web/HTTP)  
[postman - send API requests and get response data](https://learning.postman.com/docs/sending-requests/requests/)  



----
## Передача данных в запросе  


1. В URL запроса:   

        GET /products/123

Назначение: доступ к конкретному ресурсу.  

Flask  
```python
@app.route("/products/<int:product_id>")
def get_product(product_id):
    pass
```
     

2. Параметры запроса (Query Params):  

        GET /products?store_id=5&marketplace=oz  

Назначение: фильтрация, сортировка, пагинация и др.

Flask  
```python 
store_id = request.args.get("store_id")
```


3. Тело запроса (Request Body)  
Передаётся в POST/PUT/PATCH. Обычно JSON.  
Назначение: передача данных, создание/обновление сущностей.

Flask
```python  
data = request.get_json()
```


4. Форма (Form Data)
Типично для x-www-form-urlencoded или multipart/form-data (загрузки файлов)

Назвачение: формы с веб-страниц 

Flask
```python
request.form["username"]
request.files["file"] 
```


5. Заголовки (Headers)
Передаются в любом методе запроса. Например, Authorization, X-User-ID, Content-Type.

Назначение: авторизация, метаинформация

Flask
``` python
token = request.headers.get("Authorization")
```


6. Cookies
Хранятся в браузере и автоматически отправляются при запросах:

Назначение: сессии, авторизация

```python
request.cookies.get("session_id")
```
