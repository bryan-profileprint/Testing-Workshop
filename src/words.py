import re

def get_word_count(content):
    content = content.lower()
    words = re.findall(r"\w+", content)
    word_count = {}
    for word in words:
        if word not in word_count.keys():
            word_count[word] = 0
        word_count[word] += 1
    return word_count

def get_top_word(content):
    word_count = get_word_count(content)
    max_count = word_count.values()

    return [word for word, count in word_count.items()
            if count == max_count]
