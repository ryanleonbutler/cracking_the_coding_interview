from typing import Dict


def count_char_map(string: str) -> Dict:
    map = {}
    for char in string:
        if char not in map:
            map[char] = 0
        map[char] += 1
    return map


def is_unique(string: str) -> bool:
    if not isinstance(string, str):
        return False

    if len(string) == 0:
        return False

    char_map = count_char_map(string)

    for val in char_map.values():
        if val > 1:
            return False

    return True
