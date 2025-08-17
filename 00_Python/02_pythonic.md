# Pythonic

**ЧТО ЗНАЧИТ PYTHONIC?**  
На официальном сайте python.org не раскрывается это понятие.

Понятие PYTHONIC было впервые использовано разработчиком python (Tim Peters, 1999):

```
    "Pythonic means using Python idioms well, in a way that is natural for Python. 
    Unpythonic means you’re writing Python as if it were C (or Lisp, or Perl, or whatever)."
```

Приницпы PEP-20 Zen of Python(Tim Peters, 2004) полностью отражают суть Pythonic кода.  
Эти принципы стали базой для определения Pythonic.

PYTHONIC это:

1. Читаемость и простота:

   - Лаконичность не в ущерб пониманию  
   - Использование говорящих имен переменных и функций  
   - Код следует принципу "Читается как английский текст"  

1. Использование встроенных возможностей python:

   - Вместо for i in range(len(list)) использовать for item in list  
   - Вместо if x == True: использовать if x:  
   - Использование списковых включений (list comprehensions) вместо громоздких for-циклов  

1. Принятие принципов Zen of Python (import this):

   - Простое лучше сложного  
   - Явное лучше неявного  
   - Читаемость имеет значение  

1. Идиоматичность:

   - Использование синтаксического сахара  
   - Использование enumerate вместо ручного счетчика  
   - Использование zip() для итерации по нескольким спискам  
   - Примнение with open() as f: для работы с файлами  

1. Следование PEP-8:

   - Отступы 4 пробела, а не табы    
   - Максимальная длинна строки 79 символов  
   - Использование snake_case для переменных и функций  
   - Использование CamelCase для классов  

**PYTHONIC REFERENCES**

1. import this  
1. [PEP 8 – Стиль написания кода на Python](https://peps.python.org/pep-0008/)  
1. [PEP 257 – Документирование кода](https://peps.python.org/pep-0257/)  


---
## Annex

> [!NOTE] Pythonic examples

**Одновременный доступ к индексу и элементу - enumerate**

```python
# Плохая практика
for i in range(len(my_list)):
    print(i, my_list[i])

# Pythonic
for index, item in enumerate(my_list):
    print(index, item)
```

**Итерация по нескольким спискам**

```python
names = ["Алиса", "Боб"]
scores = [90, 85]

# Плохая практика
for i in range(len(names)):
    print(names[i], scores[i])

# Pythonic 
for name, score in zip(names, scores):
    print(name, score)
```

**Распаковка**

```python
a, b = b, a
```
