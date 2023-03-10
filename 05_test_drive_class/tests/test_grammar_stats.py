import pytest 
from lib.grammar_stats import GrammarStats

"""
Given a text with a capital letter at start and valid punctuation ending
It returns True
"""

def test_capital_letter_and_punctuation_are_valid():
    grammarstats = GrammarStats()
    result = grammarstats.check("Is this text valid?")
    assert result == True

"""
Given a text with a capital letter at start and invalid punctuation ending
It returns False
"""

def test_capital_letter_valid_but_punctuation_not_valid():
    grammarstats = GrammarStats()
    result = grammarstats.check("Is this text valid")
    assert result == False

"""
Given a text with a non capital letter at start and valid punctuation ending
It returns False
"""

def test_capital_letter_not_valid_but_punctuation_valid():
    grammarstats = GrammarStats()
    result = grammarstats.check("is this text valid?")
    assert result == False


"""
Given a text with a non capital letter at start and invalid punctuation ending
Raises exception error False
"""

def test_capital_letter_not_valid_and_punctuation_not_valid():
    grammarstats = GrammarStats()
    result = grammarstats.check("is this text valid")
    assert result == False
    

"""
Given an empty text
Raises exception error "Cannot validate empty text"
"""

def test_empty_text():
    grammarstats = GrammarStats()
    with pytest.raises(Exception) as e: 
        grammarstats.check("")
    error_message = str(e.value)
    assert error_message == "Cannot validate empty text"

"""
Given a text that returns True or False
It returns a value between 0 and 100 representing percentage that are good i.e. True
"""

def test_check_returns_true_once_percentage_good_returns_one_hundred():
    grammarstats = GrammarStats()
    grammarstats.check("Is this valid?")
    result = grammarstats.percentage_good()
    assert result == 100

def test_check_returns_true_once_false_once_percentage_good_returns_fifty():
    grammarstats = GrammarStats()
    grammarstats.check("Is this valid?")
    grammarstats.check("Is this valid")
    result = grammarstats.percentage_good()
    assert result == 50

def test_check_returns_true_none_false_once_percentage_good_returns_zero():
    grammarstats = GrammarStats()
    grammarstats.check("Is this valid")
    result = grammarstats.percentage_good()
    assert result == 0