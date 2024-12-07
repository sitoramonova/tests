import pytest
from main import strict
@strict
def sum_two(a: int, b: int) -> int:
    return a + b

# Тесты

def test_sum_two_correct_types():
    assert sum_two(1, 2) == 3

def test_sum_two_incorrect_types():
    with pytest.raises(TypeError):
        sum_two(1, 2.4)

def test_sum_two_all_incorrect():
    with pytest.raises(TypeError):
        sum_two("1", "2")
