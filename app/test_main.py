import pytest
from app.main import get_human_age


def test_zero_age():
    assert get_human_age(0, 0) == [0, 0]


def test_below_first_threshold():
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_first_threshold():
    assert get_human_age(15, 15) == [1, 1]


def test_within_second_threshold():
    assert get_human_age(23, 23) == [1, 1]


def test_second_threshold():
    assert get_human_age(24, 24) == [2, 2]


def test_within_third_threshold():
    assert get_human_age(27, 27) == [2, 2]


def test_cat_advances_dog_does_not():
    assert get_human_age(28, 28) == [3, 2]


def test_large_age():
    assert get_human_age(100, 100) == [21, 17]


def test_dog_third_threshold():
    assert get_human_age(0, 29) == [0, 3]


def test_mixed():
    assert get_human_age(15, 0) == [1, 0]
    assert get_human_age(0, 15) == [0, 1]
