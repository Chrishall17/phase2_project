import pytest 
from lib.text_includes_todo import text_includes_todo

"""
Given a text contains "TODO"
It returns True
"""
def test_text_includes_todo():
    assert text_includes_todo("TODO washing TODO") == True

"""
Given a text contains "TODO"
It returns True
"""
def test_text_includes_todo_with_punctuation():
    assert text_includes_todo("TODO: washing") == True

"""
Given a text does not contain "TODO"
It returns False
"""

def test_text_does_not_includes_todo():
    assert text_includes_todo("Done washing") == False

"""
Given a text contains "todo"
It returns True
"""

def test_text_includes_todo_lowercase():
    assert text_includes_todo("todo washing") == True

"""
Given a text contains an empty string
Raises an error
"""

def test_text_includes_empty_string():
    with pytest.raises(Exception) as e:
        text_includes_todo("")
    error_message = str(e.value)
    assert error_message == "Text is empty, not valid"