import pytest

from questions.urlify import urlify


@pytest.mark.parametrize(
    "input, expected",
    [
        ("Mr John Smith", "Mr%20John%20Smith"),
        (" Mr John Smith ", "Mr%20John%20Smith"),
        ("MrJohnSmith", "MrJohnSmith"),
        ("", ""),
        (None, ""),
        (False, ""),
        (1, ""),
    ],
)
def test_urlify(input, expected):
    assert urlify(input) == expected
