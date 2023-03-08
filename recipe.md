CHALLENGE:
1. Describe the Problem
# As a user
# So that I can keep track of my tasks
# I want to check if a text includes the string #TODO

2. Design the Function Signature
def text_includes_todo(text):
    Parameters:
        text: a string containing human-legible words
    Return:
        Either true or false depending on whether the text contains TODO (e.g. "TODO washing" returns True)
    Side effects:
        We have to consider whether TODO is uppercase or lowercase and that the correct value is returned in either instance

3. Create Examples as Tests

"""
Given a text contains "TODO"
It returns True
"""
text_includes_todo("TODO washing")
=> True

"""
Given a text contains "TODO" with punctuation
It returns True
"""
text_includes_todo("TODO: washing")
=> True

"""
Given a text does not contain "TODO"
It returns False
"""
text_includes_todo("Done: washing")
=> False

"""
Given a text contains an empty string
Raises an error
"""
text_includes_todo("")
=> Raises error "Text is empty, not valid"

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

from lib.text_includes_todo import text_includes_todo

"""
Given a text contains "TODO"
It returns True
"""
def test_text_includes_todo():
    assert text_includes_todo("TODO washing") == True


Exercise 2:
1. Describe the Problem
# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

2. Design the Function Signature
def check_my_grammar(text):
    Parameters:
        text: a string containing human-legible words and puncuation
    Returns:
        Either a string stating "Text is valid", "Text is partially valid, missing _" or raises an exception due to invalidity
    
3. Create Examples as Tests

"""
Given a text with a capital letter at start and valid punctuation ending
It returns "Text is valid"
"""
check_my_grammar("Is this text valid?")
=> "Text is valid"

"""
Given a text with a capital letter at start and invalid punctuation ending
It returns "Text is partially valid, missing punctuation ending"
"""
check_my_grammar("Is this text valid")
=> "Text is partially valid, missing punctuation ending"

"""
Given a text with a non capital letter at start and valid punctuation ending
It returns "Text is partially valid, missing capital letter"
"""
check_my_grammar("is this text valid?")
=> "Text is partially valid, missing capital letter"

"""
Given a text with a non capital letter at start and invalid punctuation ending
Raises exception error "Text is invalid"
"""
check_my_grammar("is this text valid")
=> "Text is invalid"

"""
Given an empty text
Raises exception error "Cannot validate empty text"
"""
check_my_grammar("")
=> "Cannot validate empty text"

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

################################################################################################

EXERCISE 1:
1. Describe the Problem
***
A program that allows me to manage my time as it allows me to estimate how long it will take to read a text. Assuming that I can read 200 words a minute. The program should tell me the time in minutes it takes to read a given text.
***

2. Design the Function Signature
def time_to_read_text(text):
    *** Extracts the time to read the given string input 

    Parameters:
        text: a string containing words (e.g. "There once was a man who lived in a house")

    Returns:
        A float stating the time in minutes that it will take to read the text with a rate of 200 words per minute 

    Side effects:
        This function doesn't print anything or have any other side effects
    ***

3. Create Examples as Tests

"""
Given a text with no words
It returns a string with "Text is empty"
"""
time_to_read_text("") => "Text is empty"

"""
Given a string with 20 words
It returns a float below 1
"""
time_to_read_text("1 2 ... 20") => 0.1

"""
Given a string with 200 words
It returns a float of 1
"""
time_to_read_text("1 2 ... 200") => 1

"""
Given a value that isn't a string
It throws an error
"""
extract_uppercase(Int) throws an error


4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.time_to_read_text import *

"""
Given a text with no words
It returns a string with "Text is empty"
"""
cxz
def test_time_to_read_empty_string_throws_message_back():
    assert time_to_read_text("") == "Text is empty"