# SQL - ОСНОВНЫЕ ОПЕРАЦИИ   

## Содержание 

[Основные операции](#Основные-операции)  
[Сложные запросы](#Сложные-запросы)
[Прочие операторы](#Прочие-операторы)
[Запросы и подзапросы](#Запросы-и-подзапросы)
[Темы ищут место](#Темы-ищут-место)

----  
## Основные операции  
**DML (DATA MANIPULATION LANGUAGE)**  

C - create:    

    INSERT INTO <table_name> () VALUES ();  

R - read:    

    SELECT * FROM <table_name>;  
    SELECT DISTINCT * FROM <table_name>;  
    JOIN  

U - update:    

    UPDATE <table_name> SET foo = bar WHERE <condition>;  

D - delete:    

    DELETE FROM <table_name> WHERE <condition>;  

**DDL (DATA DEFENITION LANGUAGE)**    

    CREATE TABLE <table_name> ();   
    
    DROP TABLE <table_name>;    

    ALTER TABLE <table_name> [ADD <column_name> / DROP COLUMN <column_name] <data_type> <constraints>;  

**DCL (DATA CONTROL LANGUAGE)**    

**TCL (TRANSACTION CONTROL LANGUAGE)**    

----
## Сложные запросы 
JOIN  
LEFT JOIN  
RIGHT JOIN  
INNER JOIN  

----
## Прочие операторы
ANY  
SOME  
UNION [ALL]  

----
## Запросы и подзапросы

----
## Темы ищут место
ACID - атомарность, согласованность, изоляция, долговечность
