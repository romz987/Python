# Имена методов производных классов выбраны
# таким образом (не отражают суть метода)
# для лаконичности програмного кода в рамках конкретной задачи
# где усложнение (ИМХО) не имеет практического смысла
# и может быть избыточно


from abc import ABC, abstractmethod


class Worker(ABC):


    @abstractmethod 
    def __init__(self, name: str):
        pass

    @abstractmethod 
    def job_one(self) -> str:
        pass 

    @abstractmethod 
    def job_two(self) -> str:
        pass


class Tiler(Worker):
    """ Класс плиточник """

    def __init__(self):
        pass

    def job_one(self) -> str:
        """ Подготовка пола """
        return "Пол подготовлен" 

    def job_two(self) -> str:
        """ Укладка плитки """
        return "Плитка уложена"


class Finisher(Worker):
    """ Класс отделочник """

    def __init__(self):
        pass

    def job_one(self) -> str:
        """ Подготовка пола """
        return "Шпаклевка нанесена" 

    def job_two(self) -> str:
        """ Укладка плитки """
        return "Стена отштукатурена"


class Painter(Worker):
    """ Класс маляр """

    def __init__(self):
        pass

    def job_one(self) -> str:
        """ Загрунтовать стену """
        return "Стена загрунтована" 

    def job_two(self) -> str:
        """ Покрасить стену """
        return "Стена покрашена"



class Chief:
    """ Прораб """

    def __init__(self):
        pass

    def create_floors(self, worker: Tiler):
        """ Сделать полы """
        print(worker.job_one())
        print(worker.job_two())

    def level_walls(self, worker: Finisher):
        """ Выровнить стены """
        print(worker.job_one())
        print(worker.job_two())

    def paint_walls(self, worker: Painter):
        """ Покрасить стены """
        print(worker.job_one())
        print(worker.job_two())

    def turnkey_work(self, tiler: Tiler, finisher: Finisher, painter: Painter):
        """ Работы под ключ """
        self.create_floors(tiler)
        self.level_walls(finisher)
        self.paint_walls(painter)


if __name__ == "__main__":
    tiler = Tiler()
    finisher = Finisher()
    painter = Painter()

    chief = Chief()
    chief.turnkey_work(tiler, finisher, painter)

