from lib.high_value import *

def test_correct_return_when_first_value_higher():
    high_value = HighValue(4,2)
    result = high_value.get_highest()
    assert result == "First value is higher"

def test_correct_return_when_second_value_higher():
    high_value = HighValue(2,4)
    result = high_value.get_highest()
    assert result == "Second value is higher"

def test_correct_return_when_equal():
    high_value = HighValue(2,2)
    result = high_value.get_highest()
    assert result == "Values are equal"

