# Python: Main Info  

## Содержание  

[Полезные ссылки](#Полезные-ссылки)    
[Общие сведения](#Общие-сведения)  
[Pythonic](#Pythonic)  
[Good Python Code](#Good-Python-Code)  
[CI and Makefile](#CI-and-Makefile)  
[Pythonic examples](#Pythonic-examples)  



----
## Полезные ссылки
Самые полезные  
[Roadmap Python](https://roadmap.sh/python)
[Real Python](https://realpython.com/)

Остальные  
[Неофициальный перевод официального руководства](https://digitology.tech/docs/python_3/tutorial/introduction.html)  
[Про Python от Selectel](https://selectel.ru/blog/courses/course-python/?utm_source=habr.com&utm_medium=referral&utm_campaign=academy_news_pythoncourse_310125_academy)  



----
## Общие сведения
Какой ты, Python?

1.Я язык с динамической типизацией:  

    Тип переменной определяется во время выполнения, а не компиляции

2.Я язык с сильной типизацией:  

    То есть, я не выполняю неявные приведения типов между несовместимыми типами (как JavaScript, например).
    И не дам тебе сложить строку и число. (зато дам умножить, но это исключение)
    А вот JavaScript - язык со слабой типизаций и даст сложить число и строку.

3.Я язык с утиной типизацией:   

    в JAVA, например, можно явно указать для функции экземпляром какого класса должен быть переданный аргумент.
    И если это условие не выполняется, функция вернет ошибку.



----
## Pythonic 
**ЧТО ЗНАЧИТ PYTHONIC?**  
На официальном сайте python.org не раскрывается это понятие.

Понятие PYTHONIC было впервые использовано разработчиком python (Tim Peters, 1999):  

        "Pythonic means using Python idioms well, in a way that is natural for Python. 
        Unpythonic means you’re writing Python as if it were C (or Lisp, or Perl, or whatever)."

Приницпы PEP-20 Zen of Python(Tim Peters, 2004) полностью отражают суть Pythonic кода.  
Эти принципы стали базой для определения Pythonic.

PYTHONIC это:  

1. Читаемость и простота:    
    - Лаконичность не в ущерб пониманию    
    - Использование говорящих имен переменных и функций    
    - Код следует принципу "Читается как английский текст"  

2. Использование встроенных возможностей python:  
    - Вместо for i in range(len(list)) использовать for item in list   
    - Вместо if x == True: использовать if x:  
    - Использование списковых включений (list comprehensions) вместо громоздких for-циклов  

3. Принятие принципов Zen of Python (import this):  
    - Простое лучше сложного  
    - Явное лучше неявного  
    - Читаемость имеет значение   

4. Идиоматичность:  
    - Использование синтаксического сахара
    - Использование enumerate вместо ручного счетчика   
    - Использование zip() для итерации по нескольким спискам  
    - Примнение with open() as f: для работы с файлами     

5. Следование PEP-8:  
    - Отступы 4 пробела, а не табы (сомнительная хуйня)  
    - Максимальная длинна строки 79 символов  
    - Использование snake_case для переменных и функций  
    - Использование CamelCase для классов  
  
**ССЫЛКИ НА ИСТОЧНИК ПОНЯТИЯ PYTHONIC**  
1. import this  
2. [PEP 8 – Стиль написания кода на Python](https://peps.python.org/pep-0008/)  
3. [PEP 257 – Документирование кода](https://peps.python.org/pep-0257/)



----
## Good Python Code 
Принципы "Хорошего" Python кода:

1. Читаемость:  
    - Именование  
    - PEP-8(импорты: strandart library, third-party, local imports, констатны(MAX_SIZE=), etc) 
    - Комментарии  

2. Эффективность и оптимизация:
    - KISS (избегание сложности)
    - Генераторы (yield)
    - Встроенные функции (map(), filter(), list comprehensions, dict comprehensions)

3. Документирование
    - Docstrings (PEP-257)
    - Типизация: аннотации типов (PEP 484)

4. Тестируемость
    - Модульность (код разбит на небольшие функции, классы)
    - Чистые функции (минимизация побочных эффектов)
    - Unit-тесты (использование pytest/unittest)

6. Идиоматичность (Pythonic way)
    - Контекстные менеджеры 
    - Распаковка (a, b = b, a)
    - Использование '_' для неиспользуемых переменных (for _ in ...)

7. Безопасность и обработка ошибок
    - LBYL vs EAFP

8. Совместимость и зависимости
    - Виртуальные окружения (venv, poetry, etc)
    - Requirements: указание версий пакетов

Литература:  
1. "Чистый Python: тонкости программирования для профи" - Дэн Бейдер
2. "Python. К вершинам мастерства" - Лучано Рамальо
3. "Python. Лучшие практики и инструменты" - Бретт Слаткин
4. Официальная документация: docs.python.org/3/ - разделы "Учебник" и "Стиль кода"



----
## CI and Makefile
GitHub Actions, Makefile и "requirements stack step" в контексте CI/CD



----
## Pythonic examples 
Одновременный доступ к индексу и элементу
```python
# Плохая практика
for i in range(len(my_list)):
    print(i, my_list[i])

# Pythonic
for index, item in enumerate(my_list):
    print(index, item)
``` 


Итерация по нескольким спискам
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


Распаковка
```python
a, b = b, a
```
