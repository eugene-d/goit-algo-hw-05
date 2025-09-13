import os


def read_file(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' not found")

    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def select_test_patterns(text, max_pattern_length=20):
    clean_text = text.replace('\n', ' ').replace('\r', ' ')
    words = clean_text.split()

    middle_words = words[len(words)//3:2*len(words)//3]

    existing_pattern = None
    for word in middle_words:
        clean_word = ''.join(c for c in word if c.isalnum())
        if 3 <= len(clean_word) <= max_pattern_length:
            existing_pattern = clean_word
            break

    if not existing_pattern:
        start_pos = len(text) // 3
        existing_pattern = text[start_pos:start_pos + 10].strip()

    non_existing_pattern = "неіснуючийтекст"

    return {
        'existing': existing_pattern,
        'non_existing': non_existing_pattern
    }



def format_time(seconds):
    ms = seconds * 1000
    return f"{ms:.3f} мс"


def print_separator(title="", char="=", width=80):
    if title:
        title_with_spaces = f" {title} "
        padding = (width - len(title_with_spaces)) // 2
        separator = char * padding + title_with_spaces + char * padding
        if len(separator) < width:
            separator += char
    else:
        separator = char * width

    print(separator)

