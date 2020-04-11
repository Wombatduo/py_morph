import unittest
from langs.EnglishVerb import EnglishVerb


class EnglishVerbTest(unittest.TestCase):

    def test_get_infinitive_for_be(self):
        self.assertEqual( "be", EnglishVerb("be").get_infinitive())

    def test_be_should_be_different_for_3_persons_singular(self):
        self.assertEqual("am", EnglishVerb("be").morph(1, 1, 2, 'M'))
        self.assertEqual("are", EnglishVerb("be").morph(2, 1, 2, 'M'))
        self.assertEqual("is", EnglishVerb("be").morph(3, 1, 2, 'M'))

    def test_be_should_be_are_for_3_persons_plural(self):
        self.assertEqual("are", EnglishVerb("be").morph(1, 2, 2, 'M'))
        self.assertEqual("are", EnglishVerb("be").morph(2, 2, 2, 'M'))
        self.assertEqual("are", EnglishVerb("be").morph(3, 2, 2, 'M'))


    def test_get_infinitive_for_do(self):
        self.assertEqual(EnglishVerb("do").get_infinitive(), "do")

    def test_do_should_be_different_for_3_persons_singular(self):
        self.assertEqual("do", EnglishVerb("do").morph(1, 1, 2, 'M'))
        self.assertEqual("do", EnglishVerb("do").morph(2, 1, 2, 'M'))
        self.assertEqual("does", EnglishVerb("do").morph(3, 1, 2, 'M'))




if __name__ == '__main__':
    unittest.main()
