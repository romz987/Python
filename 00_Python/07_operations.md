# Basic operations in Python

## Table of Contents

- [Abstracts](#Abstracts)
- [Basic operations](#Basic-operations)
  - [Assignment Operations](#Assignment-Operations)
  - [Arithmetic Operations](#Arithmetic-Operations)
  - [Comparison Operations](#Comparison-Operations)
  - [Identity Operations](#Identity-Operations)
  - [Logical Operations](#Logical-Operations)
  - [Membership Operations](#Membership-Operations)
  - [Bitwise Operations](#Bitwise-Operations)
- [DataTypes availible operations](#DataTypes-availible-operations)
  - [String](#String)
  - [List](#List)
  - [Dictionary](#Dictionary)
  - [Numeric](#Numeric)
- [Cross DataTypes operations](#Cross-DataTypes-operations)
- [Annex A: DataTypes availible operations scheme](#Annex-A)
- [Annex B: Cross DataTypes operations](#Annex-B)

______________________________________________________________________

## Abstracts

Краткий обзор (конспект) основных операций в Python.\
Обзор операций, доступных для части основных типов данных: String, List, Dictionary, Numeric.\
А так же операций, допустимых между различными типами данных.

______________________________________________________________________

## Basic operations

#### Assignment Operations

Операции присваивания

```
=   простое присваивание
+=  присваивание с операцией сложения
-=  присваивание с операцией вычитания
*=  присваивание с операцией умножения
/=  присваивание с операцией деления
```

#### Arithmetic Operations

Арифметические операции

```
+   сложение
-   вычитание 
*   умножение 
/   деление
//  целочисленное деление 
%   остаток от деления
**  возведение в степень
```

#### Comparison Operations

Операции сравнения

```
==  равно
!=  не равно
>   больше
<   меньше
>=  больше или равно
<=  меньше или равно
```

#### Identity Operations

Операции проверки идентичности

```
is       ссылаются ли переменные на один и тот же объект
is not   не ссылаются ли переменные на один и тот же объект
```

#### Logical Operations

Логические операции

```
and
or  
not
```

#### Membership Operations

Операции принадлежности

```
in 
not in
```

#### Bitwise Operations

Побитовые операции

```
&     AND 
|     OR 
^     XOR 
~     NOT
<<    Сдвиг влево
>>    Сдвиг вправо
```

#### Set operations

Операции с множествами (только set, frozenset)

```
|   объединение ( исключение: dict | dict )
&   пересечение
-   разность
^   симметрическая разность
```

______________________________________________________________________

## DataTypes availible operations

#### String

Операции присваивания
Операции сравнения
Арифметические операции
Операции идентичности
Операции вхождения

#### List

Операции присваивания
Операции сравнения
Арифметические операции
Операции идентичности
Операции вхождения

#### Dictionary

Операции присваивания
Операции сравнения
Операции идентичности
Операции вхождения

#### Numeric

**integer**
Все, кроме операции вхождения
**float**
Все, кроме побитовые и операции вхождения

______________________________________________________________________

## Cross DataTypes operations

1. Конкатенация - работает только для одинаковых sequences: str + str, list + list, tuple + tuple и(!) int + float
1. Арифметика - работает только для чисел. Исключения: * умножение для повторения sequences, + для их конкатенации
1. Повторение - работает для sequence * int

______________________________________________________________________

## Annex A: DataTypes availible operations scheme

**Операции, доступные для различных типов данных**
![datatypes-methods](./images/07_operations/operations.svg
