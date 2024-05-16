import unittest
from io import StringIO
from unittest.mock import patch

from main import main


class TestMain(unittest.TestCase):
    @patch("builtins.input", return_value="Test")
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_stdout(self, mock_stdout, mock_input):
        main()
        self.assertEqual(mock_stdout.getvalue(), 'Hello, world!\nHello, Test!\n')
    
    @patch("builtins.input", return_value="Test")
    def test_main_return(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            mock_input.assert_called_once_with("What is your name? ")


if __name__ == "__main__":
    unittest.main()
