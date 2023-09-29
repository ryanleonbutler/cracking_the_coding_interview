def compress_string(string: str) -> str:
    compressed_string = ""

    if not isinstance(string, str) or len(string) == 0:
        return compressed_string

    i = 0
    while i < len(string):
        current_char = string[i]

        count = 1
        for next_char in string[i + 1 : :]:
            if current_char == next_char:
                count += 1
            else:
                break

        compressed_string += current_char
        if count > 1:
            compressed_string += str(count)

        i += count

    return compressed_string
