import unittest
from unittest.mock import patch
from weather import get_temp,is_hot

class TestTemp(unittest.TestCase):

    @patch('weather.get_temp')
    def test_is_hot_true(self,mock_get_temp):
        mock_get_temp.return_value=45
        self.assertTrue(is_hot("Lahore",40))
        mock_get_temp.assert_called_once_with("Lahore")

    @patch('weather.get_temp')
    def test_is_hot_false(self,mock_get_temp):
        mock_get_temp.return_value=28
        self.assertFalse(is_hot("Lahore",28))
        mock_get_temp.assert_called_once_with("Lahore")

    

if __name__=="__main__":
    unittest.main()