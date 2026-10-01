import pytest
from lib.password_checker import *

def test_password_invalid():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("1234567")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."