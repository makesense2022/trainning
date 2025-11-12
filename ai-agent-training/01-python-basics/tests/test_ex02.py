"""
测试文件: ex02_numbers.py
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "exercises"))

from ex02_numbers import (
    add_numbers, divide_numbers, integer_divide,
    power, modulo, round_number
)


def test_add_numbers():
    assert add_numbers(5, 3) == 8
    assert add_numbers(-5, 3) == -2
    assert add_numbers(0, 0) == 0


def test_divide_numbers():
    result = divide_numbers(10, 3)
    assert isinstance(result, float)
    assert abs(result - 3.3333333333333335) < 0.0001
    
    result = divide_numbers(10, 2)
    assert result == 5.0
    assert isinstance(result, float)


def test_integer_divide():
    assert integer_divide(10, 3) == 3
    assert integer_divide(10, 2) == 5
    assert integer_divide(7, 2) == 3


def test_power():
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(10, 0) == 1


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(10, 2) == 0
    assert modulo(7, 3) == 1


def test_round_number():
    assert round_number(3.14159) == 3.0
    assert round_number(3.14159, 2) == 3.14
    assert round_number(3.14159, 4) == 3.1416

