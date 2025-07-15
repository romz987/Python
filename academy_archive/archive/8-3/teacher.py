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
                print(f'Учитель:\n {teacher}\n проведет консультацию в аудитории {aud} {date}')





if __name__ == "__main__":

    students = {
        'Максим': None,
        'Георгий': None,
        'Федор': None,
        'Николай': None,
        'Степан': None
    }

    tr = Teacher(students)
    # Проверим список студентов
    print(tr.get_students_dict())

    # Наймем трех учителей
    print('Наймем трех учителей')
    tr.hire_teacher('Иван Петрович', 'Химия', '10 лет', 'МГТУ')
    tr.hire_teacher('Дмитрий Иванович', 'Биология', '11 лет', 'ПГТУ')
    tr.hire_teacher('Аркадий Валерьевич', 'ОБЖ', '8 лет', 'ВГТРК')
    # Проверим результат
    print()
    print('Список учителей:')
    for teacher in tr.get_teachers_list():
        print(teacher)

    # Уволим учителя
    fired_teacher_name = 'Иван Петрович'
    print()
    print(f'Уволим учителя {fired_teacher_name}')
    tr.fire_teacher('Иван Петрович')

    # Проверим спиок учителей
    print()
    print('Список учителей:')
    for teacher in tr.get_teachers_list():
        print(teacher)

    # Узнаем имя учителя, который преподает предмет
    discipline = 'Биология'
    print()
    print(f'{discipline} преподает {tr.get_teacher_name(discipline)}')
    # Узнаеи его стаж
    print(f'Стаж учителя {tr.get_teacher_name(discipline)}: {tr.get_teacher_exp(tr.get_teacher_name(discipline))}')
    # Узнаем его ообразование
    print(f'Образование учителя {tr.get_teacher_name(discipline)}: {tr.get_teacher_education(tr.get_teacher_name(discipline))}')

    # Поставим оценку ученику
    student_name = "Федор"
    discipline = 'ОБЖ'
    mark = '5'
    print()
    print(f'Поставим оценку {mark} ученику {student_name} по предмету {discipline}')
    tr.add_mark('Федор', 'ОБЖ', '5')
    # Проверим
    print()
    for key, value in tr.get_students_dict().items():
        print(f'{key}: {value}')


    # Удалим оценку ученика
    student_name = "Федор"
    tr.remove_mark(student_name)
    # Проверим
    print()
    for key, value in tr.get_students_dict().items():
        print(f'{key}: {value}')

    # Запросим консульацию
    tr.demand_consultation('Аркадий Валерьевич', '9', '14.09.2026')

    print('buy')
