def text_includes_todo(text):
    text_upper = text.upper()
    if text == "":
        raise Exception("Text is empty, not valid")
    return text_upper.count("TODO") > 0