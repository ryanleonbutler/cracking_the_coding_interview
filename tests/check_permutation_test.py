import pytest

from questions.check_permutation import check_permutation


@pytest.mark.parametrize(
    "input_1, input_2, expected",
    [
        ("tested", "test", True),
        ("blah", "blah", True),
        ("ilovecake", "yolo", False),
        (None, None, False),
        ("", "", False),
    ],
)
def test_func(input_1, input_2, expected):
    assert check_permutation(input_1, input_2) == expected
