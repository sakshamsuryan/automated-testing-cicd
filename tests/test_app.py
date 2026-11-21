import pytest
from app import add, divide, get_user_status


def test_add():
    assert add(5, 3) == 8


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_adult_status():
    assert get_user_status(21) == "Adult"


def test_minor_status():
    assert get_user_status(15) == "Minor"
