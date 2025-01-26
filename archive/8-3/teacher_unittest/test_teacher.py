import unittest 
from teacher import Teacher 

class TestTeacher(unittest.TestCase):


    def setUp(self):
        self.students = {
            'Максим': None,
            'Георгий': None,
            'Федор': None,
            'Николай': None,
            'Степан': None
        }
        self.teacher = Teacher(self.students)


    def test_hire_teacher(self):
        self.teacher.hire_teacher('Иван Петрович', 'Химия', '10 лет', 'МГТУ')
        self.assertEqual(len(self.teacher.teachers_list), 1)
        self.assertTrue(self.teacher.check_teacher_name('Иван Петрович'))


    def test_fire_teacher(self):
        self.teacher.hire_teacher('Иван Петрович', 'Химия', '10 лет', 'МГТУ')
        self.teacher.fire_teacher('Иван Петрович')
        self.assertEqual(len(self.teacher.teachers_list), 0)
        self.assertFalse(self.teacher.check_teacher_name('Иван Петрович'))


    def test_add_mark(self):
        self.teacher.hire_teacher('Иван Петрович', 'Химия', '10 лет', 'МГТУ')
        self.teacher.add_mark('Максим', 'Химия', '5')
        self.assertEqual(self.teacher.get_students_dict()['Максим'], 'оценка: 5, предмет: Химия, учитель: Иван Петрович')


    def test_remove_mark(self):
        self.teacher.hire_teacher('Иван Петрович', 'Химия', '10 лет', 'МГТУ')
        self.teacher.add_mark('Максим', 'Химия', '5')
        self.teacher.remove_mark('Максим')
        self.assertIsNone(self.teacher.get_students_dict()['Максим'])


    def test_demand_consultation(self):
        self.teacher.hire_teacher('Иван Петрович', 'Химия', '10 лет', 'МГТУ')
        result = self.teacher.demand_consultation('Иван Петрович', '101', '01.01.2023')
        self.assertEqual(result, 'Иван Петрович проведет консультацию в аудитории 101 01.01.2023')


    def test_get_teacher_exp(self):
        self.teacher.hire_teacher('Иван Петрович', 'Химия', '10 лет', 'МГТУ')
        exp = self.teacher.get_teacher_exp('Иван Петрович')
        self.assertEqual(exp, '10 лет')


    def test_get_teacher_education(self):
        self.teacher.hire_teacher('Иван Петрович', 'Химия', '10 лет', 'МГТУ')
        education = self.teacher.get_teacher_education('Иван Петрович')
        self.assertEqual(education, 'МГТУ')


    def test_get_teacher_discipline(self):
        self.teacher.hire_teacher('Иван Петрович', 'Химия', '10 лет', 'МГТУ')
        discipline = self.teacher.get_teacher_discipline('Иван Петрович')
        self.assertEqual(discipline, 'Химия')



if __name__ == '__main__':
    unittest.main()
