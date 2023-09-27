from typing import Dict


def char_map(word: str) -> Dict:
    map = {}
    for char in word:
        if char not in map:
            map[char] = 0
        map[char] += 1
    return map


def one_away(word_one: str, word_two: str) -> bool:
    # check if words are both strings
    if not isinstance(word_one, str) or not isinstance(word_two, str):
        return False

    # if len diff > 1 then than translates to more than 1 change and we don't need to check anything else
    if abs(len(word_one) - len(word_two)) > 1:
        return False

    # create a map with the counts
    word_one_map = char_map(word_one)
    word_two_map = char_map(word_two)

    edit_count = 0
    for char, count in word_two_map.items():
        if not word_one_map.get(char):
            edit_count += 1
        if count != word_one_map.get(char, 0):
            edit_count += 1

    if edit_count > 1:
        return False
    else:
        return True
