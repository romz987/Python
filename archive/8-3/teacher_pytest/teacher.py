from abc import ABC, abstractmethod


class AbstractTeacher(ABC):
    """ Абстрактный класс учитель """


    @abstractmethod 
    def get_teachers_list(self):
        """ Вернуть список учителей """
        pass


    @abstractmethod 
    def get_students_dict(self):
        """ Вернуть список студентов """


    @abstractmethod 
    def hire_teacher(self):
        """ Нанять учителя """
        pass


    @abstractmethod 
    def check_teacher_name(self):
        """ Проверить существует ли учитель"""
        pass


    @abstractmethod 
    def fire_teacher(self):
        """ Уволить учителя """
        pass


    @abstractmethod 
    def get_teacher_name(self):
        """ Вернуть имя учителя """
        pass


    @abstractmethod 
    def get_teacher_exp(self):
        """ Вернуть стаж учителя"""
        pass


    @abstractmethod 
    def get_teacher_education(self):
        """ Вернуть образование учителя """
        pass


    @abstractmethod 
    def get_teacher_discipline(self):
        """ 
        Вернуть название преподаваемого предмета
        """
        pass


    @abstractmethod 
    def add_mark(self):
        """ Поставить оценку """
        pass
        

    @abstractmethod 
    def remove_mark(self):
        """ Поставить оценку """
        pass


    @abstractmethod 
    def demand_consultation(self):
        """ Провести консультацию """
        pass
    

class Teacher(AbstractTeacher):

    teachers_list = []


    def __init__(self, students: dict):
        self.__students = students
        pass


    def get_teachers_list(self) -> list:
        return self.teachers_list


    def get_students_dict(self) -> dict:
        return self.__students


    def check_teacher_name(self, name: str) -> bool:
        for teacher in self.teachers_list:
            if name in teacher:
                return True 

        return False


    def hire_teacher(self, name: str, discipline: str, exp: str, education: str) -> None:
        teacher_exist = self.check_teacher_name(name)
        if not teacher_exist:
            teacher_dict = {}
            teacher_dict[name] = [discipline, exp, education]
            self.teachers_list.append(teacher_dict)


    def fire_teacher(self, name: str) -> None:
        for teacher in self.teachers_list:
            if name in teacher:
                self.teachers_list.remove(teacher)


    def get_teacher_name(self, discipline: str) -> str:
        for teacher in self.teachers_list:
            for key, value in teacher.items():
                if discipline == value[0]:
                    return key


    def get_teacher_exp(self, name: str) -> str:
        for teacher in self.teachers_list:
            for key, value in teacher.items():
                if name == key:
                    return value[1]
                

    def get_teacher_education(self, name: str) -> str:
        for teacher in self.teachers_list:
            for key, value in teacher.items():
                if name == key:
                    return value[2]


    def get_teacher_discipline(self, name: str) -> str:
        for teacher in self.teachers_list:
            for key, value in teacher.items():
                if name == key:
                    return value[0]


    def add_mark(self, student_name:str, discipline: str, mark: str) -> None:
        for teacher in self.teachers_list:
            for key, value in teacher.items():
                if discipline in value:
                    teacher_name = key
        for key, value in self.__students.items():
            if student_name == key:
                self.__students[key] = f'оценка: {mark}, предмет: {discipline}, учитель: {teacher_name}'


    def remove_mark(self, student_name) -> None:
        for key, value in self.__students.items():
            if student_name == key:
                self.__students[key] = None


    def demand_consultation(self, name: str, aud: str, date: str) -> None:
        for teacher in self.teachers_list:
            if name in teacher:
                key = list(teacher.keys())[0]
                return f'{key} проведет консультацию в аудитории {aud} {date}'

