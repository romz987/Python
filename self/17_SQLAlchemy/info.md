# SQLAlchemy

## Содержание  
[Добавление данных](#Добавление-данных)
[Получение данных](#Получение-данных)
[Специальные методы](#Специальные-методы)


## Добавление данных  
ADD   
Назначение: Добавляет объект в сессию для последующего INSERT  
```python
object = Model(key=value)  
db.session.add(object)  
db.session.commit()
```

MERGE
Назначение: "Подтягивает" состояние объекта в сессию (SELECT + INSERT/UPDATE).
```python
record = Model(id=1, name="Updated Name")
db.session.merge(record)  # Если id=1 существует, обновит запись
db.session.commit()
```

DELETE 
Назначение: Помечает объект для удаления.
```python
record = StoreModel.query.get(1)
db.session.delete(record)
db.session.commit()  # Выполнит DELETE
```

EXPIRE 
Назначение: Сбрасывает загруженные атрибуты объекта (при следующем обращении к ним будет выполнен SELECT).
```python
store = StoreModel.query.get(1)
db.session.expire(store)  # Следующий доступ к store.name вызовет запрос к БД
```


REFRESH
Назначение: Немедленно перезагружает состояние объекта из БД

BULK_SAVE_OBJECTS
Назначение: Массовая вставка/обновление (без вызова событий SQLAlchemy)

BULK_INSERT_MAPPING
Назначение: Массовая вставка через словари (высокая производительность)



## Получение данных
QUERY.GET()  
Получение по первичному ключу
```python
store = StoreModel.query.get(1)  # Возвращает StoreModel или None
```


QUERY.FIRST()
Первая запись
```python 
store = StoreModel.query.filter_by(marketplace='wb').first()
```


QUERY.ALL()
Все записи
```python
all_stores = StoreModel.query.all()  # Список всех StoreModel
```


QUERY.FILTER_BY()
Фильтрация по точным значениям
```python
wb_stores = StoreModel.query.filter_by(marketplace='wb').all()
```


QUERY.FILTER()
Гибкая фильтрация (с условиями)
```python
from sqlalchemy import or_
stores = StoreModel.query.filter(
    or_(
        StoreModel.marketplace == 'wb',
        StoreModel.created_at > datetime(2024, 1, 1)
    ).all()
```


МЕТОДЫ АГРЕГАЦИИ
QUERY.COUNT()
Количество записей
```python
count = StoreModel.query.filter_by(marketplace='oz').count()
```


QUERY.WITH_ENTITIES()
Выбор конкретных полей
```python 
names = StoreModel.query.with_entities(StoreModel.store_name).all()
```


QUERY.DISCTINCT()
Уникальные значения 
```python 
unique_markets = StoreModel.query.with_entities(
    StoreModel.marketplace
).distinct().all()
```


## Сложные запросы (SQLAlchemy Core)
SELECT()
Современный стиль (SQLAlchemy 2.x)
```python
from sqlalchemy import select
stmt = select(StoreModel).where(StoreModel.marketplace == 'wb')
stores = db.session.execute(stmt).scalars().all()
```


TEXT()
RAW SQL (для сложных случаев) 
```python
from sqlalchemy import text
result = db.session.execute(text("SELECT * FROM stores WHERE marketplace='oz'"))
```


## Оптимизированные запросы
QUERY.JOIN()
Соединение таблиц
```python
stores_with_products = StoreModel.query.join(ProductModel).all()
```


QUERY.OPTIONS()
Жадная загрузка 
```python
from sqlalchemy.orm import joinedload
stores = StoreModel.query.options(joinedload(StoreModel.products)).all()
```



## Специальные методы для работы с транзакциями
COMMIT()   
Фиксирует все изменения в БД  
  
ROLLBACK()   
Откатывает несохраненные изменения  
  
BEGIN NESTED()  
Создает вложенную транзакцию (полезно для частичных откатов)  



## Методы для запросов
EXECUTE  
Выполняет произвольный SQL-запрос или выражение SQLAlchemy

SCALARS
Возвращает результаты запроса в виде скалярных значений



