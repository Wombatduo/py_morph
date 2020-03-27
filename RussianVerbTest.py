import unittest
from EnglishVerb import EnglishVerb, Person, Number
from RussianVerb import RussianVerb


class RussianVerbTest(unittest.TestCase):

    def test_get_infinitive_for_быть(self):
        self.assertEqual( "быть", RussianVerb("быть").get_infinitive())

    def test_быть_should_be_different_for_3_persons_singular(self):
        self.assertEqual(RussianVerb("есть").morph(1, 1, 2, 'M'))
        self.assertEqual("are", EnglishVerb("be").morph(2, 1, 2, 'M'))
        self.assertEqual("is", EnglishVerb("be").morph(3, 1, 2, 'M'))

if __name__ == '__main__':
    unittest.main()
