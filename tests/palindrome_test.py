import pytest

from questions.palindrome import is_palindrome


@pytest.mark.parametrize(
    "string, permutation, expected",
    [
        ("taco cat", "atco cta", True),
        ("I love cake", "I vole ekca", True),
        ("I love cake", "this is great", False),
        ("", "", False),
        (1, 2, False),
        ("", "i love cake", False),
    ],
)
def test_is_palindrome(string, permutation, expected):
    assert is_palindrome(string, permutation) == expected
