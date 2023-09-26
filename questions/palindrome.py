from typing import Dict


def char_map(string: str) -> Dict:
    map = {}

    for char in string.replace(" ", ""):
        if char not in map:
            map[char] = 0
        map[char] += 1

    return map


def is_palindrome(string: str, permutation: str) -> bool:
    if not isinstance(string, str) or not isinstance(permutation, str) or len(string) == 0 or len(permutation) == 0:
        return False

    strings_word_list = string.split(" ")
    permutation_word_list = permutation.split(" ")

    for i in range(len(strings_word_list)):
        word_char_map = char_map(strings_word_list[i])
        palindrome_perm_word_map = char_map(permutation_word_list[i])
        if word_char_map == palindrome_perm_word_map:
            return True

    return False
