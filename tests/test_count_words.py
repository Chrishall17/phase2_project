from lib.count_words import *

def test_function_returns_string_count_zero_when_empty():
    result = count_words("")
    assert result == 0

def test_function_returns_string_count_when_not_empty():
    result = count_words("This string has four")
    assert result == 4

def test_function_returns_string_count_when_comma_included():
    result = count_words("This,string,has,four")
    assert result == 4

def test_function_returns_string_count_when_dot_included():
    result = count_words("This.string.has.four")
    assert result == 4