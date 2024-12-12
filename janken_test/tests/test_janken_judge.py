import unittest
from unittest.mock import patch
from source.janken_judge import judge

class TestJudgeFunction(unittest.TestCase):

    @patch('builtins.print')
    def test_draw(self, mock_print):
        self.assertEqual(judge('グー', 'グー'), 'draw')
        mock_print.assert_called_with("あいこ")

    @patch('builtins.print')
    def test_player_win(self, mock_print):
        self.assertEqual(judge('チョキ', 'グー'), 'player_win')
        mock_print.assert_called_with("あなたの勝ち！")

    @patch('builtins.print')
    def test_computer_win(self, mock_print):
        self.assertEqual(judge('グー', 'チョキ'), 'computer_win')
        mock_print.assert_called_with("あなたの負け...")

if __name__ == '__main__':
    unittest.main()
