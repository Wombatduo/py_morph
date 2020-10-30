import unittest
from langs.russian.RussianVerb import RussianVerb


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

    def test_do_should_be_different_for_3_persons_singular(self):
        self.assertEqual("делаю", RussianVerb("делать").morph(1, 1, 2, 'M'))
        self.assertEqual("делаешь", RussianVerb("делать").morph(2, 1, 2, 'M'))
        self.assertEqual("делает", RussianVerb("делать").morph(3, 1, 2, 'M'))

    def test_do_should_be_different_for_3_persons_past_singular(self):
        self.assertEqual("делал", RussianVerb("делать").morph(1, 1, 1, 'M'))
        self.assertEqual("делал", RussianVerb("делать").morph(2, 1, 1, 'M'))
        self.assertEqual("делал", RussianVerb("делать").morph(3, 1, 1, 'M'))

    def test_do_should_be_different_for_3_persons_future_singular(self):
        self.assertEqual("буду делать", RussianVerb("делать").morph(1, 1, 3, 'M'))
        self.assertEqual("будешь делать", RussianVerb("делать").morph(2, 1, 3, 'M'))
        self.assertEqual("будет делать", RussianVerb("делать").morph(3, 1, 3, 'M'))

    def test_do_should_be_different_for_3_persons_plural(self):
        self.assertEqual("делаем", RussianVerb("делать").morph(1, 2, 2, 'M'))
        self.assertEqual("делаете", RussianVerb("делать").morph(2, 2, 2, 'M'))
        self.assertEqual("делают", RussianVerb("делать").morph(3, 2, 2, 'M'))

    def test_do_should_be_different_for_3_persons_past_plural(self):
        self.assertEqual("делали", RussianVerb("делать").morph(1, 2, 1, 'M'))
        self.assertEqual("делали", RussianVerb("делать").morph(2, 2, 1, 'M'))
        self.assertEqual("делали", RussianVerb("делать").morph(3, 2, 1, 'M'))

    def test_do_should_be_different_for_3_persons_future_plural(self):
        self.assertEqual("будем делать", RussianVerb("делать").morph(1, 2, 3, 'M'))
        self.assertEqual("будете делать", RussianVerb("делать").morph(2, 2, 3, 'M'))
        self.assertEqual("будут делать", RussianVerb("делать").morph(3, 2, 3, 'M'))

    def test_be_should_be_same_for_3_persons(self):
        self.assertEqual("есть", RussianVerb("быть").morph(1, 1, 2, 'M'))
        self.assertEqual("есть", RussianVerb("быть").morph(2, 1, 2, 'M'))
        self.assertEqual("есть", RussianVerb("быть").morph(3, 1, 2, 'M'))
        self.assertEqual("есть", RussianVerb("быть").morph(1, 2, 2, 'M'))
        self.assertEqual("есть", RussianVerb("быть").morph(2, 2, 2, 'M'))
        self.assertEqual("есть", RussianVerb("быть").morph(3, 2, 2, 'M'))

    def test_do_should_be_same_for_3_persons_past_singular(self):
        self.assertEqual("был", RussianVerb("быть").morph(1, 1, 1, 'M'))
        self.assertEqual("был", RussianVerb("быть").morph(2, 1, 1, 'M'))
        self.assertEqual("был", RussianVerb("быть").morph(3, 1, 1, 'M'))

    def test_do_should_be_same_for_3_persons_past_plural(self):
        self.assertEqual("были", RussianVerb("быть").morph(1, 2, 1, 'M'))
        self.assertEqual("были", RussianVerb("быть").morph(2, 2, 1, 'M'))
        self.assertEqual("были", RussianVerb("быть").morph(3, 2, 1, 'M'))

    def test_do_should_be_different_for_3_persons_future_singular(self):
        self.assertEqual("буду", RussianVerb("быть").morph(1, 1, 3, 'M'))
        self.assertEqual("будешь", RussianVerb("быть").morph(2, 1, 3, 'M'))
        self.assertEqual("будет", RussianVerb("быть").morph(3, 1, 3, 'M'))

    def test_do_should_be_different_for_3_persons_future_plural(self):
        self.assertEqual("будем", RussianVerb("быть").morph(1, 2, 3, 'M'))
        self.assertEqual("будете", RussianVerb("быть").morph(2, 2, 3, 'M'))
        self.assertEqual("будут", RussianVerb("быть").morph(3, 2, 3, 'M'))

    def test_can_should_be_different_for_3_persons_present(self):
        self.assertEqual("могу",   RussianVerb("мочь").morph(1, 1, 2, 'M'))
        self.assertEqual("можешь", RussianVerb("мочь").morph(2, 1, 2, 'M'))
        self.assertEqual("может",  RussianVerb("мочь").morph(3, 1, 2, 'M'))
        self.assertEqual("можем",  RussianVerb("мочь").morph(1, 2, 2, 'M'))
        self.assertEqual("можете", RussianVerb("мочь").morph(2, 2, 2, 'M'))
        self.assertEqual("могут",  RussianVerb("мочь").morph(3, 2, 2, 'M'))

    def test_can_should_be_same_for_3_persons_past(self):
        self.assertEqual("мог", RussianVerb("мочь").morph(1, 1, 1, 'M'))
        self.assertEqual("мог", RussianVerb("мочь").morph(2, 1, 1, 'M'))
        self.assertEqual("мог", RussianVerb("мочь").morph(3, 1, 1, 'M'))
        self.assertEqual("могли", RussianVerb("мочь").morph(1, 2, 1, 'M'))
        self.assertEqual("могли", RussianVerb("мочь").morph(2, 2, 1, 'M'))
        self.assertEqual("могли", RussianVerb("мочь").morph(3, 2, 1, 'M'))

    def test_can_should_be_different_for_3_persons_future(self):
        self.assertEqual("смогу", RussianVerb("мочь").morph(1, 1, 3, 'M'))
        self.assertEqual("сможешь", RussianVerb("мочь").morph(2, 1, 3, 'M'))
        self.assertEqual("сможет", RussianVerb("мочь").morph(3, 1, 3, 'M'))
        self.assertEqual("сможем", RussianVerb("мочь").morph(1, 2, 3, 'M'))
        self.assertEqual("сможете", RussianVerb("мочь").morph(2, 2, 3, 'M'))
        self.assertEqual("смогут", RussianVerb("мочь").morph(3, 2, 3, 'M'))

    def test_say_should_be_different_for_3_persons_present(self):
        self.assertEqual("скажу",   RussianVerb("сказать").morph(1, 1, 2, 'M'))
        self.assertEqual("скажешь", RussianVerb("сказать").morph(2, 1, 2, 'M'))
        self.assertEqual("скажет",  RussianVerb("сказать").morph(3, 1, 2, 'M'))
        self.assertEqual("скажем",  RussianVerb("сказать").morph(1, 2, 2, 'M'))
        self.assertEqual("скажете", RussianVerb("сказать").morph(2, 2, 2, 'M'))
        self.assertEqual("скажут",  RussianVerb("сказать").morph(3, 2, 2, 'M'))

    def test_say_should_be_same_for_3_persons_past(self):
        self.assertEqual("сказал", RussianVerb("сказать").morph(1, 1, 1, 'M'))
        self.assertEqual("сказал", RussianVerb("сказать").morph(2, 1, 1, 'M'))
        self.assertEqual("сказал", RussianVerb("сказать").morph(3, 1, 1, 'M'))
        self.assertEqual("сказали", RussianVerb("сказать").morph(1, 2, 1, 'M'))
        self.assertEqual("сказали", RussianVerb("сказать").morph(2, 2, 1, 'M'))
        self.assertEqual("сказали", RussianVerb("сказать").morph(3, 2, 1, 'M'))

    def test_say_should_be_different_for_3_persons_future(self):
        self.assertEqual("скажу", RussianVerb("сказать").morph(1, 1, 3, 'M'))
        self.assertEqual("скажешь", RussianVerb("сказать").morph(2, 1, 3, 'M'))
        self.assertEqual("скажет", RussianVerb("сказать").morph(3, 1, 3, 'M'))
        self.assertEqual("скажем", RussianVerb("сказать").morph(1, 2, 3, 'M'))
        self.assertEqual("скажете", RussianVerb("сказать").morph(2, 2, 3, 'M'))
        self.assertEqual("скажут", RussianVerb("сказать").morph(3, 2, 3, 'M'))

    def test_see_should_be_different_for_3_persons(self):
        self.assertEqual("вижу", RussianVerb("видеть").morph(1, 1, 2, 'M'))
        self.assertEqual("видишь", RussianVerb("видеть").morph(2, 1, 2, 'M'))
        self.assertEqual("видит", RussianVerb("видеть").morph(3, 1, 2, 'M'))
        self.assertEqual("видим", RussianVerb("видеть").morph(1, 2, 2, 'M'))
        self.assertEqual("видите", RussianVerb("видеть").morph(2, 2, 2, 'M'))
        self.assertEqual("видят", RussianVerb("видеть").morph(3, 2, 2, 'M'))

    def test_see_should_be_different_for_3_persons_past(self):
        self.assertEqual("видел", RussianVerb("видеть").morph(1, 1, 1, 'M'))
        self.assertEqual("видел", RussianVerb("видеть").morph(2, 1, 1, 'M'))
        self.assertEqual("видел", RussianVerb("видеть").morph(3, 1, 1, 'M'))
        self.assertEqual("видели", RussianVerb("видеть").morph(1, 2, 1, 'M'))
        self.assertEqual("видели", RussianVerb("видеть").morph(2, 2, 1, 'M'))
        self.assertEqual("видели", RussianVerb("видеть").morph(3, 2, 1, 'M'))

    def test_see_should_be_different_for_3_persons_future(self):
        self.assertEqual("буду видеть", RussianVerb("видеть").morph(1, 1, 3, 'M'))
        self.assertEqual("будешь видеть", RussianVerb("видеть").morph(2, 1, 3, 'M'))
        self.assertEqual("будет видеть", RussianVerb("видеть").morph(3, 1, 3, 'M'))
        self.assertEqual("будем видеть", RussianVerb("видеть").morph(1, 2, 3, 'M'))
        self.assertEqual("будете видеть", RussianVerb("видеть").morph(2, 2, 3, 'M'))
        self.assertEqual("будут видеть", RussianVerb("видеть").morph(3, 2, 3, 'M'))

    def test_want_should_be_different_for_3_persons(self):
        self.assertEqual("хочу", RussianVerb("хотеть").morph(1, 1, 2, 'M'))
        self.assertEqual("хочешь", RussianVerb("хотеть").morph(2, 1, 2, 'M'))
        self.assertEqual("хочет", RussianVerb("хотеть").morph(3, 1, 2, 'M'))
        self.assertEqual("хотим", RussianVerb("хотеть").morph(1, 2, 2, 'M'))
        self.assertEqual("хотите", RussianVerb("хотеть").morph(2, 2, 2, 'M'))
        self.assertEqual("хотят", RussianVerb("хотеть").morph(3, 2, 2, 'M'))

    def test_want_should_be_different_for_3_persons_past(self):
        self.assertEqual("хотел", RussianVerb("хотеть").morph(1, 1, 1, 'M'))
        self.assertEqual("хотел", RussianVerb("хотеть").morph(2, 1, 1, 'M'))
        self.assertEqual("хотел", RussianVerb("хотеть").morph(3, 1, 1, 'M'))
        self.assertEqual("хотели", RussianVerb("хотеть").morph(1, 2, 1, 'M'))
        self.assertEqual("хотели", RussianVerb("хотеть").morph(2, 2, 1, 'M'))
        self.assertEqual("хотели", RussianVerb("хотеть").morph(3, 2, 1, 'M'))

    def test_want_should_be_different_for_3_persons_future(self):
        self.assertEqual("буду хотеть", RussianVerb("хотеть").morph(1, 1, 3, 'M'))
        self.assertEqual("будешь хотеть", RussianVerb("хотеть").morph(2, 1, 3, 'M'))
        self.assertEqual("будет хотеть", RussianVerb("хотеть").morph(3, 1, 3, 'M'))
        self.assertEqual("будем хотеть", RussianVerb("хотеть").morph(1, 2, 3, 'M'))
        self.assertEqual("будете хотеть", RussianVerb("хотеть").morph(2, 2, 3, 'M'))
        self.assertEqual("будут хотеть", RussianVerb("хотеть").morph(3, 2, 3, 'M'))

    if __name__ == '__main__':
        unittest.main()
