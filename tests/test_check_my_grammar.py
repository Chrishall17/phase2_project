import pytest 
from lib.check_my_grammar import check_my_grammar

"""
Given a text with a capital letter at start and valid punctuation ending
It returns "Text is valid"
"""

def test_capital_letter_and_punctuation_are_valid():
    assert check_my_grammar("Is this text valid?") == "Text is valid"

"""
Given a text with a capital letter at start and invalid punctuation ending
It returns "Text is partially valid, missing punctuation ending"
"""

def test_capital_letter_valid_but_punctuation_not_valid():
    assert check_my_grammar("Is this text valid") == "Text is partially valid, missing punctuation ending"

"""
Given a text with a non capital letter at start and valid punctuation ending
It returns "Text is partially valid, missing capital letter"
"""

def test_capital_letter_not_valid_but_punctuation_valid():
    assert check_my_grammar("is this text valid?") == "Text is partially valid, missing capital letter"

"""
Given a text with a non capital letter at start and invalid punctuation ending
Raises exception error "Text is invalid"
"""

def test_capital_letter_not_valid_and_punctuation_not_valid():
    assert check_my_grammar("is this text valid") == "Text is invalid"

"""
Given an empty text
Raises exception error "Cannot validate empty text"
"""

def test_empty_text():
    with pytest.raises(Exception) as e: 
        check_my_grammar("")
    error_message = str(e.value)
    assert error_message == "Cannot validate empty text"