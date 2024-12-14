class Employer:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        """Выводит информацию о служащем"""
        print("Служащий: ", self.name)

    def __str__(self):
        return f"Служащий: {self.name}, Возраст: {self.age}"

    def __int__(self):
        return self.age


class President(Employer):
    def print_info(self):
        print(f"Президент: {self.name}, Возраст: {self.age}")

    def __str__(self):
        return f"Президент: {self.name}, Возраст: {self.age}"


class Manager(Employer):
    def print_info(self):
        print(f"Менеджер: {self.name}, Возраст: {self.age}")

    def __str__(self):
        return f"Менеджер: {self.name}, Возраст: {self.age}"


class Worker(Employer):
    def print_info(self):
        print(f"Рабочий: {self.name}, Возраст: {self.age}")

    def __str__(self):
        return f"Рабочий: {self.name}, Возраст: {self.age}"


if __name__ == "__main__":
    president = President("Иван Иванов", 50)
    manager = Manager("Петр Петров", 35)
    worker = Worker("Сидор Сидоров", 28)

    president.print_info()  
    manager.print_info()
    worker.print_info()

    print(str(president))
    print(int(president))

    print(str(manager))
    print(int(manager))      

    print(str(worker))
    print(int(worker))

