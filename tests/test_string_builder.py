from lib.string_builder import *

def test_string_adding():
    empty = StringBuilder()
    empty.add("hello")
    empty.add(" world")
    result = empty.output()
    assert result == "hello world"

def test_length_of_string():
    empty = StringBuilder()
    empty.add("hello world")
    result = empty.size()
    assert result == 11