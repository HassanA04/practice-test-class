from lib.gratitudes import *

def test_adding_one_gratitude():
    empty = Gratitudes()
    empty.add("Technology")
    result = empty.format()
    assert result == "Be grateful for: Technology"

def test_adding_multiple_gratitudes():
    empty = Gratitudes()
    empty.add("Technology")
    empty.add("Coke zero")
    empty.add("Oxygen")
    result = empty.format()
    assert result == "Be grateful for: Technology, Coke zero, Oxygen"