# extend the map with any other url encoded char's you need
url_encode_map = {
    " ": "%20",
}


def urlify(string: str) -> str:
    urlify_string = ""

    if not isinstance(string, str):
        return urlify_string

    for char in string.strip():
        urlify_string += url_encode_map.get(char, char)
    return urlify_string
