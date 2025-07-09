def get_num_words(text):
    words = text.split()
    return len(words)

def get_each_char(text):
    text = text.lower()
    d = {}
    for char in text:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d

def get_sorted_chars(chars):
    sorted_chars = []
    for char in chars:
        sorted_chars.append({"char": char, "num": chars[char]})
    def sort_on(pair):
        return pair["num"]
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars