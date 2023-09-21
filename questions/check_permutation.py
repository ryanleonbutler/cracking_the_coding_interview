def char_count_map(string):
    map = {}

    for char in string:
        if char not in map:
            map[char] = 0
        map[char] += 1

    return map


def check_permutation(string, sub_string):
    if not isinstance(string, str) or not isinstance(sub_string, str):
        return False

    if len(string) == 0 or len(sub_string) == 0:
        return False

    string_map = char_count_map(string)
    sub_string_map = char_count_map(sub_string)

    for char, count in sub_string_map.items():
        if char not in string_map.keys() or count > string_map.get(char, 0):
            return False

    return True
