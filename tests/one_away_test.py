import pytest

from questions.one_away import one_away


@pytest.mark.parametrize(
    "word_one, word_two,  expected",
    [
        ("pale", "ple", True),
        ("pale", "bake", False),
        ("test", "te", False),
        ("test", "tes", True),
        # ("ilovecake", "cakelovei", False),  # TODO: need to check each index as well
    ],
)
def test_one_away(word_one, word_two, expected):
    assert one_away(word_one, word_two) == expected
