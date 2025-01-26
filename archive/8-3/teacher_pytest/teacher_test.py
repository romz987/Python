import pytest 
from teacher import Teacher


@pytest.fixture
def sample_instance():
    students = {
        'Максим': None,
        'Георгий': None,
        'Федор': None,
        'Николай': None,
        'Степан': None
    }
    return Teacher(students)


def test_hire_teacher(sample_instance):
    th = sample_instance
    th.hire_teacher('Иван Петрович', 'Химия', '11 лет', 'МГТУ')
    assert len(th.teachers_list) == 1
    assert th.teachers_list[0] == {'Иван Петрович': ['Химия', '11 лет', 'МГТУ']}


def test_fire_teacher(sample_instance):
    th = sample_instance
    th.hire_teacher('Иван Петрович', 'Химия', '11 лет', 'МГТУ')
    th.fire_teacher('Иван Петрович')
    assert len(th.teachers_list) == 0


def test_get_teachers_list(sample_instance):
    th = sample_instance 
    th.hire_teacher('Иван Петрович', 'Химия', '11 лет', 'МГТУ')
    th.hire_teacher('Дмитрий Иванович', 'Биология', '11 лет', 'ПГТУ')
    th.hire_teacher('Аркадий Валерьевич', 'ОБЖ', '8 лет', 'ВГТРК')
    assert th.get_teachers_list() == [
        {'Иван Петрович': ['Химия', '11 лет', 'МГТУ']}, 
        {'Дмитрий Иванович': ['Биология', '11 лет', 'ПГТУ']}, 
        {'Аркадий Валерьевич': ['ОБЖ', '8 лет', 'ВГТРК']}
    ]


def test_get_teacher_name(sample_instance):
    th = sample_instance
    th.hire_teacher('Иван Петрович', 'Химия', '11 лет', 'МГТУ')
    th.hire_teacher('Дмитрий Иванович', 'Биология', '11 лет', 'ПГТУ')
    th.hire_teacher('Аркадий Валерьевич', 'ОБЖ', '8 лет', 'ВГТРК')
    assert th.get_teacher_name('Биология') == 'Дмитрий Иванович'


def test_get_teacher_exp(sample_instance):
    th = sample_instance
    th.hire_teacher('Иван Петрович', 'Химия', '11 лет', 'МГТУ')
    th.hire_teacher('Дмитрий Иванович', 'Биология', '11 лет', 'ПГТУ')
    th.hire_teacher('Аркадий Валерьевич', 'ОБЖ', '8 лет', 'ВГТРК')
    assert th.get_teacher_exp('Аркадий Валерьевич') == '8 лет'


def test_get_teacher_education(sample_instance):
    th = sample_instance
    th.hire_teacher('Иван Петрович', 'Химия', '11 лет', 'МГТУ')
    th.hire_teacher('Дмитрий Иванович', 'Биология', '11 лет', 'ПГТУ')
    th.hire_teacher('Аркадий Валерьевич', 'ОБЖ', '8 лет', 'ВГТРК')
    assert th.get_teacher_education('Аркадий Валерьевич') == 'ВГТРК'


def test_get_teacher_discipline(sample_instance):
    th = sample_instance
    th.hire_teacher('Иван Петрович', 'Химия', '11 лет', 'МГТУ')
    th.hire_teacher('Дмитрий Иванович', 'Биология', '11 лет', 'ПГТУ')
    th.hire_teacher('Аркадий Валерьевич', 'ОБЖ', '8 лет', 'ВГТРК')
    assert th.get_teacher_discipline('Иван Петрович') == 'Химия'


def test_add_mark(sample_instance):
    th = sample_instance
    th.hire_teacher('Иван Петрович', 'Химия', '11 лет', 'МГТУ')
    th.hire_teacher('Дмитрий Иванович', 'Биология', '11 лет', 'ПГТУ')
    th.hire_teacher('Аркадий Валерьевич', 'ОБЖ', '8 лет', 'ВГТРК')
    th.add_mark('Георгий', 'ОБЖ', '5')
    assert th.get_students_dict()['Георгий'] == 'оценка: 5, предмет: ОБЖ, учитель: Аркадий Валерьевич'


def test_remove_mark(sample_instance):
    th = sample_instance
    th.hire_teacher('Иван Петрович', 'Химия', '11 лет', 'МГТУ')
    th.hire_teacher('Дмитрий Иванович', 'Биология', '11 лет', 'ПГТУ')
    th.hire_teacher('Аркадий Валерьевич', 'ОБЖ', '8 лет', 'ВГТРК')
    th.add_mark('Георгий', 'ОБЖ', '5')
    th.remove_mark('Георгий')
    assert th.get_students_dict()['Георгий'] == None


def test_demand_consultation(sample_instance):
    th = sample_instance
    th.hire_teacher('Иван Петрович', 'Химия', '11 лет', 'МГТУ')
    th.hire_teacher('Дмитрий Иванович', 'Биология', '11 лет', 'ПГТУ')
    th.hire_teacher('Аркадий Валерьевич', 'ОБЖ', '8 лет', 'ВГТРК')
    result = th.demand_consultation('Дмитрий Иванович', '11', '22-09-25')
    assert result == 'Дмитрий Иванович проведет консультацию в аудитории 11 22-09-25' 
