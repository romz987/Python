# Python: списковые и словарные выражения.    
    
    
## Содержание    
  
[Списковые выражения](#Списковые-выражения)    
[Словарные выражения](#Словарные-выражения)  
[Создаем список словарей](#Создаем-список-словарей)    
  
  
## Списковые выражения
**List comprehensions**      
Это компактный способ создать список на основе итерируемого объекта.  
Основными преимуществами списковых выражений python являются скорость работы и читаемость. Списковые выражения работают быстрее, чем циклы for потому что полностью реализованы на C.  

Простой пример:
```python   
# Суть  
[выражение for элемент in итерируемый_объект if условие]   
  
squares = [x**2 for x in range(5)]   
```    

Списковые выражения c условиями:
```python 
result_list = []
for x in range(10):
    if x % 2 == 0:
        result_list.append(x) 
# Аналогично 
result_list = [x for x in range(10) if x % 2 == 0]


result_list = []   
for x in range(-3, 3):
    if x > 0:
        result_list.append(x)
    else:
        result_list.append(0)
# Аналогично 
[x if x > 0 else 0 for x in range(-3, 3)]
```



## Словарные выражания
**Dict comprehensions**   
Словарные выражения обладают такими же преимуществами, как и списковые.  

Простой пример:
```python   
{x: x**2 for x in range(5)}
# Результат
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

Пример посложнее:
```python  

```

Словарные выражения с условиями
```python

```



## Cоздаем список словарей 
В данном случае all_records - это 


return [
    {
        "id": rc.id,
        "mp_articul": rc.mp_articul,
        "additional_cost": rc.additional_cost,
        "element_name": rc.element_name,
        "element_articul": rc.element_articul,
        "store_id": rc.store_id,
    }
    for rc in all_records
]
