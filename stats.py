
"""
def count_words(text):
    words = text.split()
    return len(words)
"""

def count_characters(text):
    char_count = {}
    text = text.lower()

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_characters(char_count_dict):
    char_list = []
    for char, count in char_count_dict.items():
        if char.isalpha():
            char_list.append({"char" : char, "num": count})

    char_list.sort(key=lambda x: x["num"], reverse=True)

    return char_list