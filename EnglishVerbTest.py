import unittest
from EnglishVerb import EnglishVerb, Person, Number


class EnglishVerbTest(unittest.TestCase):

    def test_be_should_be_different_for_3_persons_singular(self):
        self.assertEqual("am", EnglishVerb("be").morph(Person.FIRST, Number.SINGULAR, "Present", 'M'))
        self.assertEqual("are", EnglishVerb("be").morph(Person.SECOND, Number.SINGULAR, "Present", 'M'))
        self.assertEqual("is", EnglishVerb("be").morph(Person.THIRD, Number.SINGULAR, "Present", 'M'))

    def test_be_should_be_are_for_3_persons_plural(self):
        self.assertEqual("are", EnglishVerb("be").morph(Person.FIRST, Number.PLURAL, "Present", 'M'))
        self.assertEqual("are", EnglishVerb("be").morph(Person.SECOND, Number.PLURAL, "Present", 'M'))
        self.assertEqual("are", EnglishVerb("be").morph(Person.THIRD, Number.PLURAL, "Present", 'M'))

    def test_get_infinitive(self):
        self.assertEqual(EnglishVerb("be").get_infinitive(), "be")


if __name__ == '__main__':
    unittest.main()
