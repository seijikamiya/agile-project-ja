from calculator import add, subtract, root, div, is_numeric, exp
from unittest.mock import patch

#Tests for add function
@patch('builtins.input', side_effect=['10', '20'])
def test_add_case1(mock_input):
    assert add() == 30

@patch('builtins.input', side_effect=["-1", "0"])
def test_add_case2(mock_input):
    assert add() == -1

@patch('builtins.input', side_effect=["2.5", "-1.0"])
def test_add_case3(mock_input):
    assert add() == 1.5

@patch('builtins.input', side_effect=["a", "b"])
def test_add_case4(mock_input):
    assert add() == None

#Tests for subtract function
@patch('builtins.input', side_effect=['20', '10'])
def test_subtract_case1(mock_input):
    assert subtract() == 10

@patch('builtins.input', side_effect=["0", "0"])
def test_subtract_case2(mock_input):
    assert subtract() == 0

@patch('builtins.input', side_effect=["2.5", "1.0"])
def test_subtract_case3(mock_input):
    assert subtract() == 1.5

@patch('builtins.input', side_effect=["-2.5", "-1.0"])
def test_subtract_case4(mock_input):
    assert subtract() == -1.5

@patch('builtins.input', side_effect=["a", "b"])
def test_subtract_case5(mock_input):
    assert subtract() == None

#Tests for exp function
@patch('builtins.input', side_effect=['2', '2'])
def test_exp_case1(mock_input):
    assert exp() == 4

@patch('builtins.input', side_effect=["2", "-1"])
def test_exp_case2(mock_input):
    assert exp() == 0.5

@patch('builtins.input', side_effect=["-2", "-1"])
def test_exp_case3(mock_input):
    assert exp() == -0.5

@patch('builtins.input', side_effect=["0", "2"])
def test_exp_case4(mock_input):
    assert exp() == 0

@patch('builtins.input', side_effect=["2", "0"])
def test_exp_case5(mock_input):
    assert exp() == 1

@patch('builtins.input', side_effect=["a", "b"])
def test_exp_case6(mock_input):
    assert exp() == None

#Tests for root function
@patch('builtins.input', side_effect=['4'])
def test_root_case1(mock_input):
    assert root() == 2

@patch('builtins.input', side_effect=["-1"])
def test_root_case2(mock_input):
    assert root() == None

@patch('builtins.input', side_effect=["e"])
def test_root_case3(mock_input):
    assert root() == None

#Tests for div function
@patch('builtins.input', side_effect=['20', '10'])
def test_div_case1(mock_input):
    assert div() == 2

@patch('builtins.input', side_effect=["-3.2", "2"])
def test_div_case2(mock_input):
    assert div() == -1.6

@patch('builtins.input', side_effect=["10", "0"])
def test_div_case3(mock_input):
    assert div() == None

@patch('builtins.input', side_effect=["a", "b"])
def test_div_case4(mock_input):
    assert div() == None

#Tests for is_numeric function
def test_is_numeric_case1():
    assert is_numeric('4') == True

def test_is_numeric_case2():
    assert is_numeric('-3.1') == True

def test_is_numeric_case3():
    assert is_numeric("e") == False