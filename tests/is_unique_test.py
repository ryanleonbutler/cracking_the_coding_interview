import pytest

from questions.is_unique import is_unique


@pytest.mark.parametrize(
    "input, expected",
    [
        ("abcdef", True),
        ("asdf", True),
        ("aaaaaaaaaaa", False),
        ("aabbaabb", False),
        ("cccccccc", False),
        ("yolo", False),
        ("", False),
        (None, False),
    ],
)
def test_is_unique(input, expected):
    assert is_unique(input) == expected
