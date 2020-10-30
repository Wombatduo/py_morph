import unittest
from langs.german.GermanVerb import GermanVerb


class GermanVerbTest(unittest.TestCase):

    def test_get_infinitive_for_be(self):
        self.assertEqual("sein", GermanVerb("sein").get_infinitive())

    def test_should_be_different_for_3_persons_singular(self):
        self.assertEqual("bin", GermanVerb("sein").morph(1, 1, 2, 'M'))
        self.assertEqual("bist", GermanVerb("sein").morph(2, 1, 2, 'M'))
        self.assertEqual("ist", GermanVerb("sein").morph(3, 1, 2, 'M'))

    def test_should_be_are_for_3_persons_plural(self):
        self.assertEqual("sind", GermanVerb("sein").morph(1, 2, 2, 'M'))
        self.assertEqual("seid", GermanVerb("sein").morph(2, 2, 2, 'M'))
        self.assertEqual("sind", GermanVerb("sein").morph(3, 2, 2, 'M'))

    def test_should_be_different_for_3_persons_past_singular(self):
        self.assertEqual("war", GermanVerb("sein").morph(1, 1, 1, 'M'))
        self.assertEqual("warst", GermanVerb("sein").morph(2, 1, 1, 'M'))
        self.assertEqual("war", GermanVerb("sein").morph(3, 1, 1, 'M'))

    def test_should_be_are_for_3_persons_past_plural(self):
        self.assertEqual("waren", GermanVerb("sein").morph(1, 2, 1, 'M'))
        self.assertEqual("wart", GermanVerb("sein").morph(2, 2, 1, 'M'))
        self.assertEqual("waren", GermanVerb("sein").morph(3, 2, 1, 'M'))

    def test_should_be_different_for_3_persons_future_singular(self):
        self.assertEqual("werde sein", GermanVerb("sein").morph(1, 1, 3, 'M'))
        self.assertEqual("wirst sein", GermanVerb("sein").morph(2, 1, 3, 'M'))
        self.assertEqual("wird sein", GermanVerb("sein").morph(3, 1, 3, 'M'))

    def test_should_be_are_for_3_persons_future_plural(self):
        self.assertEqual("werden sein", GermanVerb("sein").morph(1, 2, 3, 'M'))
        self.assertEqual("werdet sein", GermanVerb("sein").morph(2, 2, 3, 'M'))
        self.assertEqual("werden sein", GermanVerb("sein").morph(3, 2, 3, 'M'))


if __name__ == '__main__':
    unittest.main()
