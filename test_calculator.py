import pytest

from calculater import addition, division, multiplication, subtraction


def test_addition():
    assert addition(5, 3) == 8


def test_addition_with_floats():
    assert addition(2.5, 10.25) == 12.75


def test_addition_with_negative_numbers():
    assert addition(-2, -12) == -14


def test_addition_with_invalid_input_raises_type_error():
    with pytest.raises(TypeError):
        addition("2", 3)


def test_addition_with_invalid_input_letter_raises_type_error():
    with pytest.raises(TypeError):
        addition("A", 3)

def test_subtraction():
    assert subtraction(9, 4) == 5


def test_subtraction_with_floats():
    assert subtraction(10.5, 2.25) == 8.25


def test_subtraction_with_negative_numbers():
    assert subtraction(-9, -4) == -5


def test_subtraction_with_invalid_input_raises_type_error():
    with pytest.raises(TypeError):
        subtraction("G", 4)


def test_subtraction_with_invalid_input_letterraises_type_error():
    with pytest.raises(TypeError):
        subtraction("G", 4)

def test_multiplication():
    assert multiplication(6, 7) == 42


def test_multiplication_with_floats():
    assert multiplication(3.5, 2.0) == 7.0


def test_multiplication_with_negative_numbers():
    assert multiplication(-6, 7) == -42


def test_multiplication_with_invalid_input_raises_type_error():
    with pytest.raises(TypeError):
        multiplication("6", "7")

def test_multiplication_with_invalid_input_letter_raises_type_error():
    with pytest.raises(TypeError):
        multiplication("D", "H")


def test_division():
    assert division(20, 4) == 5


def test_division_with_floats():
    assert division(9.0, 2.0) == 4.5


def test_division_with_negative_numbers():
    assert division(-20, 4) == -5


def test_division_with_invalid_input_raises_type_error():
    with pytest.raises(TypeError):
        division("20", 4)


def test_division_with_invalid_input_letter_raises_type_error():
    with pytest.raises(TypeError):
        division("T", 4)


def test_division_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        division(10, 0)
