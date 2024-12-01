from abc import ABC, abstractmethod


class Animals(ABC):


    @abstractmethod
    def sound(self):
        """ Печатает звук, который издает животное """
        pass

    @abstractmethod
    def show_name(self):
        """ Печатает имя животного """
        pass

    @abstractmethod
    def animal_type(self):
        """ Печататает подвид животного """
        pass



class Anim(Animals):

    def __init__(self, kind, name, sound, animal_type):
        self._kind = kind
        self._name = name.capitalize() 
        self._sound = sound
        self._animal_type = animal_type

    def sound(self):
        print(
            f'{self._kind} делает {self._sound}'
        )

    def show_name(self):
        print(
            f'это {self._kind} по имени {self._name}'
        )

    def animal_type(self):
        print(
            f'{self._kind} {self._animal_type}'
        )



if __name__ == "__main__": 

    andg = Anim('собака', 'бабака', 'буф!', 'подвид волка')
    anct = Anim('кот', 'бегемот', 'мяу!', 'подвид лесного кота')
    anpt = Anim('попугай', 'геша', 'python is a slowest language I saw ever', 'подвид динозавра')
    anhr = Anim('хомяк', 'медведь', '...', 'просто грызун')

    andg.show_name()
    andg.sound()
    andg.animal_type()
    print('')
    anct.show_name()
    anct.sound()
    anct.animal_type()
    print('')
    anpt.show_name()
    anpt.sound()
    anpt.animal_type()
    print('')
    anhr.show_name()
    anhr.sound()
    anhr.animal_type()
