import pytest
from lib.present import *

def test_wrap_a_wrapped_present():
    present = Present()
    present.wrap("Stuff")
    with pytest.raises(Exception) as e:
        present.wrap("New Stuff")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_unwrap_an_unwrapped_present():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."