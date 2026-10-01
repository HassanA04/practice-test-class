from lib.greet import *

def test_greet_returns_hello_munira():
    result = greet("munira")
    assert result == "hello munira!"