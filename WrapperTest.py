import unittest

from Wrapper import wrap

class TestEnglishVerb(unittest.TestCase):

    def test_warp(self):
        s = ""
        self.assertEqual(s, wrap(None, 1))
        self.assertEqual("x", wrap("x", 1))
        self.assertEqual("x\nx", wrap("xx", 1))
        self.assertEqual("x\nx\nx", wrap("xxx", 1))
        self.assertEqual("x\nx", wrap("x x", 1))
        self.assertEqual("x\nxx", wrap("x xx", 3))
        self.assertEqual(
            "Twas\nbrillig,\nand the\nslithy\ntoves\nDid gyre\nand\ngimble\nin the\nwabe All\nmimsy\nwere the\nborogove\ns, And\nthe mome\nraths\noutgrabe",
            wrap(
                "Twas brillig, and the slithy toves Did gyre and gimble in the wabe All mimsy were the borogoves, And the mome raths outgrabe",
                8)
        )


if __name__ == '__main__':
    unittest.main()