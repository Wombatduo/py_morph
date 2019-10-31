import unittest
from EnglishVerb import EnglishVerb


class TestEnglishVerb(unittest.TestCase):

    def test_be_in_1sPrM_shouldBe_am(self):
        self.assertEqual(EnglishVerb("be").morph(1, 's', "Present", 'M'), "am")

    def test_get_infinitive(self):
        self.assertEqual(EnglishVerb("be").get_infinitive(), "be")


if __name__ == '__main__':
    unittest.main()
