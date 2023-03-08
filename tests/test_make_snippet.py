from lib.make_snippet import *

def test_make_snippet_returns_first_five_words_and_three_dots_if_more_than_five():
    result = make_snippet("There are more than five words")
    assert result == "There are more than five..."

def test_snippet_has_less_than_five():
    result = make_snippet("There are only four")
    assert result == "There are only four"