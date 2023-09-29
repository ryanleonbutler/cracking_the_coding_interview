import pytest

from questions.string_compression import compress_string


@pytest.mark.parametrize(
    "string, expected",
    [
        ("aabcccccaaa", "a2bc5a3"),
        ("test", "test"),
        ("ilovecake", "ilovecake"),
        ("", ""),
        (1, ""),
    ],
)
def test_compress_string(string, expected):
    assert compress_string(string) == expected
