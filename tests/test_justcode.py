import pytest
from justcode import user_number_check

def test_basic_user():
    assert user_number_check(0) == "the user is just basic"
    assert user_number_check(5) == "the user is just basic"
    assert user_number_check(10) == "the user is just basic"

def test_advanced_user():
    assert user_number_check(20) == "the user is advanced"

def test_expert_user():
    assert user_number_check(30) == "the user is expert"
    assert user_number_check(40) == "the user is expert"
    assert user_number_check(100) == "the user is expert"

def test_invalid_range():
    assert user_number_check(11) == "enter the numbers from 10 to 30"
    assert user_number_check(21) == "enter the numbers from 10 to 30"
    assert user_number_check(29) == "enter the numbers from 10 to 30"
