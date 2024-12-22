from utils.utils import get_quiz_words, get_data, base_program
import unittest


class TestUtils(unittest.TestCase):

    data_to_test = get_data('questions_data/questions.json')

    questions_dict = data_to_test[0]['questions']
    levels_dict = data_to_test[1]['levels']


    def test_1_get_data(self):
        self.assertEqual(len(get_data('questions_data/questions.json')), 2)


    def test_2_get_quiz_words(self):
        self.assertEqual(len(get_quiz_words('легкий', self.questions_dict)), 5)
        self.assertEqual(get_quiz_words('средний', self.questions_dict), {
        "believe": "верить",
        "feel": "чувствовать",
        "make": "делать",
        "open": "открывать",
        "think": "думать"
      })


    def test_3_base_program(self):
        self.assertEqual(len(base_program(self.questions_dict[0])), 5)
        self.assertEqual(type(base_program(self.questions_dict[0])['family']), bool)


