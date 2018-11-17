from unittest import TestCase

from gol import GameOfLife

# given
ARRAY1 = [
    [False,  True, False],
    [False, False, False]
]

class GolTest(TestCase):

    def setUp(self):
        self.gol = GameOfLife(ARRAY1)

    def test_get_state(self):
        self.assertTrue(self.gol.get_state(0, 1))

    def test_living(self):
        self.assertEqual(self.gol.living(1, 1), 1)
