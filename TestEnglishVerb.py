import unittest
from EnglishVerb import EnglishVerb, Person


class TestEnglishVerb(unittest.TestCase):

    def test_be_in_1sPrM_shouldBe_am(self):
        self.assertEqual("am", EnglishVerb("be").morph(Person.First, 's', "Present", 'M'))
        self.assertEqual("are", EnglishVerb("be").morph(Person.Second, 's', "Present", 'M'))
        self.assertEqual("is", EnglishVerb("be").morph(Person.Third, 's', "Present", 'M'))

    def test_get_infinitive(self):
        self.assertEqual(EnglishVerb("be").get_infinitive(), "be")


if __name__ == '__main__':
    unittest.main()
