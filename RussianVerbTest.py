import unittest
from RussianVerb import RussianVerb


class RussianVerbTest(unittest.TestCase):

    def test_get_pronouns(self):
        self.assertEqual("я", RussianVerb.get_pronoun(1, 1, 1))
        self.assertEqual("ты", RussianVerb.get_pronoun(2, 1, 1))
        self.assertEqual("он", RussianVerb.get_pronoun(3, 1, 1))
        self.assertEqual("она", RussianVerb.get_pronoun(3, 1, 2))
        self.assertEqual("оно", RussianVerb.get_pronoun(3, 1, 3))
        self.assertEqual("мы", RussianVerb.get_pronoun(1, 2, 1))
        self.assertEqual("вы", RussianVerb.get_pronoun(2, 2, 1))
        self.assertEqual("они", RussianVerb.get_pronoun(3, 2, 1))

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

    def test_should_be_different_for_3_persons_plural(self):
        self.assertEqual("делаем", RussianVerb("делать").morph(1, 2, 2, 'M'))
        self.assertEqual("делаете", RussianVerb("делать").morph(2, 2, 2, 'M'))
        self.assertEqual("делают", RussianVerb("делать").morph(3, 2, 2, 'M'))

    def test_should_be_different_for_3_persons_past_plural(self):
        self.assertEqual("делали", RussianVerb("делать").morph(1, 2, 1, 'M'))
        self.assertEqual("делали", RussianVerb("делать").morph(2, 2, 1, 'M'))
        self.assertEqual("делали", RussianVerb("делать").morph(3, 2, 1, 'M'))

    def test_should_be_different_for_3_persons_future_plural(self):
        self.assertEqual("будем делать", RussianVerb("делать").morph(1, 2, 3, 'M'))
        self.assertEqual("будете делать", RussianVerb("делать").morph(2, 2, 3, 'M'))
        self.assertEqual("будут делать", RussianVerb("делать").morph(3, 2, 3, 'M'))


if __name__ == '__main__':
    unittest.main()
