from lib.time_to_read_text import *

def test_time_to_read_empty_string_throws_message_back():
    assert time_to_read_text("") == "Text is empty"

def test_time_to_read_with_ten_strings_returns_float():
    assert time_to_read_text("1 2 3 4 5 6 7 8 9 10") == 0.05

def test_time_to_read_with_twenty_strings_returns_float():
    text = " ".join(["word" for i in range(0, 20)])
    result = time_to_read_text(text)
    assert result == 0.1 