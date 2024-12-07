from task_one import Teacher


class DisciplineTeacher(Teacher):


    def __init__(self, name: str, education: str, expirience: int, discipline: str, job_title: str):
        super().__init__(name, education, expirience)
        self.__discipline = discipline
        self.__job_title = job_title


    def get_teacher_data(self):
        expirience = self.get_expirience()
        name = self.get_name()
        education = self.get_education()
        print(
            f'{name}, образование {education}, '
            f'преподаёт дисциплину {self.__discipline}, '
            f'работает в должности {self.__job_title} '
            f'опыт работы: {expirience} лет'
        )

    def set_job_title(self):
        try:
            jt = str(input(
                'Введите должность: '
                )
            )
        except Exception:
            print('Должность должна быть строкой')
            self.set_expirience()
        else:
            self.__job_title = jt
            print('Должность изменена')


    def add_mark(self, student_name: str, score: int):
        name = self.get_name()
        print(
            f'{name} поставил оценку ' 
            f'{score} студенту {student_name}, '
            f'предмет {self.__discipline}'
        )


    def remove_mark(self, student_name: str, score: int):
        name = self.get_name()
        print(
            f'{name} удалил оценку ' 
            f'{score} студенту {student_name}'
            f'предмет {self.__discipline}'
        )


    def give_a_consultation(self, auditory: str):
        name = self.get_name()
        print(
            f'{name} провел консультацию ' 
            f'в классе {auditory} '
            f'по предмету {self.__discipline} как {self.__job_title}'
        )


tch = DisciplineTeacher('Сергей Васильев', 'МФТИ', 8, 'Биология', 'Профессор')

tch.get_teacher_data()
tch.set_expirience()
tch.set_job_title()
tch.add_mark('Максим Иванов', 5)
tch.remove_mark('Владимир Петров', 4)
tch.give_a_consultation('8F')
tch.get_teacher_data()

