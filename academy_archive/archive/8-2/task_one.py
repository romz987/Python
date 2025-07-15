class Teacher:


    def __init__(self, name: str, education: str, expirience: int):
        self.__name = name
        self.__education = education 
        self.__expirience = expirience


    def get_name(self):
        return self.__name


    def get_education(self):
        return self.__education


    def get_expirience(self):
        return self.__expirience

        
    def get_teacher_data(self):
        print(
            f'{self.__name}, образование {self.__education}, ' 
            f'опыт работы: {self.__expirience} лет'
        )

    def set_expirience(self):
        try:
            exp = int(input(
                'Введите стаж в годах: '
                )
            )
        except Exception:
            print('Стаж должен быть целым числом')
            self.set_expirience()
        else:
            self.__expirience = exp
            print('Стаж изменен')


    def add_mark(self, student_name: str, score: int):
        print(
            f'{self.__name} поставил оценку ' 
            f'{score} студенту {student_name}'
        )


    def remove_mark(self, student_name: str, score: int):
        print(
            f'{self.__name} удалил оценку ' 
            f'{score} студенту {student_name}'
        )


    def give_a_consultation(self, auditory: str):
        print(
            f'{self.__name} провел консультацию ' 
            f'в классе {auditory}'
        )


# tch = Teacher('Сергей Васильев', 'МФТИ', 8)
#
# tch.get_teacher_data()
# tch.set_expirience()
# tch.add_mark('Максим Иванов', 5)
# tch.remove_mark('Владимир Петров', 4)
# tch.give_a_consultation('8F')





