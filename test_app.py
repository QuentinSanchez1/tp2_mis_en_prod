from app import soustraction

class TestAddition(unittest.TestCase):
    # tests précédents...

    def test_soustraction(self):
        self.assertEqual(soustraction(5, 3), 2)
        self.assertEqual(soustraction(0, 0), 0)
        self.assertEqual(soustraction(-1, -1), 0)
