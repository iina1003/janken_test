import unittest
from source.player import player_pon
from unittest.mock import patch

class TestPlayerPonModule(unittest.TestCase):
    @patch('builtins.input', side_effect=['0', '1'])
    def test_invalid_then_rock(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "グー")
    
    @patch('builtins.input', return_value='1')
    def test_rock(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "グー")
    
    @patch('builtins.input', return_value='2')
    def test_scissors(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "チョキ")
    
    @patch('builtins.input', return_value='3')
    def test_paper(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "パー")

    @patch('builtins.input', side_effect=['4', '2'])
    def test_invalid_then_scissors(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "チョキ")

if __name__ == '__main__':
    unittest.main()
