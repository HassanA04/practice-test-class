from lib.counter import *

def test_adding_to_count():
    zero = Counter()
    zero.add(1)
    result = zero.report()
    assert result == "Counted to 1 so far."

def test_add_multiple_times():
    zero = Counter()
    zero.add(1)
    zero.add(9)
    result = zero.report()
    assert result == "Counted to 10 so far."