import unittest

from EnglishVerb import EnglishVerb


class TestEnglishVerb(unittest.TestCase):

  def test_be_in_1sPrM_sholdBe_am(self):
      self.assertEqual(EnglishVerb("be").morph(1,'s',"Present",'M'), "am")

if __name__ == '__main__':
    unittest.main()