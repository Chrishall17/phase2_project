def count_words(str):
    new_str = str.replace(",", ", ").replace(".", ". ")
    return len(new_str.split())