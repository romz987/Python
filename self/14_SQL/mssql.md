# Microsoft SQL Server   

## Контент  
[Полезные ссылки](#Полезные-ссылки)  
[Создаем базу данных](#Создаем-базу-данных)
[Создание таблиц](#Создание-таблиц)
[Темы ищут место](#Темы-ищут-место)

----

## Полезные ссылки
[Разворачиваем RDBMS в docker](https://learn.microsoft.com/ru-ru/sql/linux/quickstart-install-connect-docker?view=sql-server-ver16&tabs=cli&pivots=cs1-bash)  \

----
## Создаем базу данных
```sql
    CREATE DATABASE EducationalDB
    ON PRIMARY 
    (
        NAME = EducationalDB_Data,
        FILENAME = '/var/opt/mssql/data/EducationalDB.mdf',
        SIZE = 15MB,
        FILEGROWTH = 15%,
        MAXSIZE = UNLIMITED
    )
    LOG ON 
    (
        NAME = EducationalDB_Log,
        FILENAME = '/var/opt/mssql/data/EducationalDB.ldf',
        SIZE = 10MB,
        FILEGROWTH = 5MB,
        MAXSIZE = 60MB
    );
```

FILEGROWTH - прирост файла при приближении к лимиту текущего установленного размера

----
## Создание таблиц 
Ограничения(Constraints): 

    PRIMARY KEY — уникальный идентификатор строки, автоматически включает NOT NULL.
    FOREIGN KEY — ссылка на другую таблицу, обеспечивает целостность данных.
    NOT NULL — запрещает NULL, требует обязательного значения.
    UNIQUE — гарантирует уникальность значений в столбце.
    CHECK — задаёт условия для допустимых значений (CHECK (age >= 18)).
    DEFAULT — устанавливает значение по умолчанию (DEFAULT GETDATE()).
    IDENTITY (только для MS SQL Server) — автоинкремент (IDENTITY(1,1)). - он же автоприращение


----
## Темы ищут место

0. Что такое collation? - набор правил определяющий кодировку, сортировку, сравнение 
1. При использовании НЕ латиницы всегда стоит использовать типы данных с поддержкой UNICODE
2. Поиск и индексация будут медленне, если в качестве первичных ключей использовать типы данных НЕ int.
