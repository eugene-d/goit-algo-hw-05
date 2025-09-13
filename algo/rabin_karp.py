def polynomial_hash(string, base=256, modulus=101):
    n = len(string)
    hash_value = 0
    for i, char in enumerate(string):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def search(text, pattern):
    if not pattern:
        return 0
    if len(pattern) > len(text):
        return -1

    pattern_length = len(pattern)
    text_length = len(text)

    base = 256
    modulus = 101

    pattern_hash = polynomial_hash(pattern, base, modulus)
    current_slice_hash = polynomial_hash(text[:pattern_length], base, modulus)

    h_multiplier = pow(base, pattern_length - 1) % modulus
    for i in range(text_length - pattern_length + 1):
        if pattern_hash == current_slice_hash:
            if text[i:i+pattern_length] == pattern:
                return i

        if i < text_length - pattern_length:
            current_slice_hash = (current_slice_hash - ord(text[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(text[i + pattern_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1
