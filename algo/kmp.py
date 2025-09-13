def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def search(text, pattern):
    if not pattern:
        return 0
    if len(pattern) > len(text):
        return -1

    pattern_length = len(pattern)
    text_length = len(text)

    lps = compute_lps(pattern)

    i = j = 0
    while i < text_length:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == pattern_length:
            return i - j
    return -1
