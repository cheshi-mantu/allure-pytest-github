import pytest
import allure

def test_example_one():
    assert 1 + 1 == 2

def test_example_two():
    assert "hello".upper() == "HELLO"

def test_example_three():
    assert len([1, 2, 3]) == 3

def test_example_four():
    assert 10 > 5

def test_example_five():
    assert isinstance(3.14, float)


