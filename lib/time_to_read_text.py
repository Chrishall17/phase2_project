def time_to_read_text(text):
    if text == "":
        return "Text is empty"
    return len(text.split()) / 200

# in video demo -> exception raised as opposed to returning an empty string and then test for error.
# tested 200 words first and error last