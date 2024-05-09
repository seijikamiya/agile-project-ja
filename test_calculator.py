from calculator import add
from unittest.mock import patch

@patch('builtins.input', side_effect=['10', '20'])
def test_add(mock_input):
    assert add() == 30