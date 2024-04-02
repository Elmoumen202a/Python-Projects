import unittest
from main import CheckSpleen

class TestCheckSpleen(unittest.TestCase):
    def test_initial_board(self):
        game = CheckSpleen()
        self.assertEqual(len(game.board), 8)
        self.assertEqual(len(game.board[0]), 8)
        self.assertEqual(game.board[0][0], '-')
        self.assertEqual(game.board[3][3], 'O')


if __name__ == '__main__':
    unittest.main()
