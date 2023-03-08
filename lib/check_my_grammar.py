def check_my_grammar(text):
    if text == "":
        raise Exception("Cannot validate empty text")
    elif text[0].isupper() and text[-1] in ".!?":
        return "Text is valid"
    elif text[0].isupper():
        return "Text is partially valid, missing punctuation ending"
    elif text[-1] in ".!?":
        return "Text is partially valid, missing capital letter"
    elif text[0].islower() and text[-1] not in ".!?":
        return "Text is invalid"
    

