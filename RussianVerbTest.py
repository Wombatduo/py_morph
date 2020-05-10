import unittest
from RussianVerb import RussianVerb


class RussianVerbTest(unittest.TestCase):

    def test_get_infinitive(self):
        self.assertEqual("быть", RussianVerb("быть").get_infinitive())

    def test_should_be_different_for_3_persons_singular(self):
        self.assertEqual("делаю", RussianVerb("делать").morph(1, 1, 2, 'M'))
        self.assertEqual("делаешь", RussianVerb("делать").morph(2, 1, 2, 'M'))
        self.assertEqual("делает", RussianVerb("делать").morph(3, 1, 2, 'M'))

    def test_should_be_different_for_3_persons_past_singular(self):
        self.assertEqual("делал", RussianVerb("делать").morph(1, 1, 1, 'M'))
        self.assertEqual("делал", RussianVerb("делать").morph(2, 1, 1, 'M'))
        self.assertEqual("делал", RussianVerb("делать").morph(3, 1, 1, 'M'))

    def test_should_be_different_for_3_persons_future_singular(self):
        self.assertEqual("буду делать", RussianVerb("делать").morph(1, 1, 3, 'M'))
        self.assertEqual("будешь делать", RussianVerb("делать").morph(2, 1, 3, 'M'))
        self.assertEqual("будет делать", RussianVerb("делать").morph(3, 1, 3, 'M'))


if __name__ == '__main__':
    unittest.main()
