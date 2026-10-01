from lib.report_length import *

def test_report_length_returns_sentence():
    result = report_length("hello")
    assert result == f"This string was 5 characters long."