import pytest 
from lib.diary_entry import DiaryEntry

"""
Given a class with a title and contents added 
It returns the title and contents in the format My title: contents
"""

def test_diary_entry_one_format():
    diaryentry = DiaryEntry("Dune", "a sci-fi epic")
    result = diaryentry.format()
    assert result == "Dune: a sci-fi epic"

def test_diary_entry_two_format():
    diaryentry = DiaryEntry("Mandalorian", "a sci-fi great")
    result = diaryentry.format()
    assert result == "Mandalorian: a sci-fi great"

"""
Given a diary entry with title and contents
It returns the no. of words in contents
"""

def test_number_of_words_in_contents_one():
    diaryentry = DiaryEntry("Mandalorian", "a sci-fi great")
    result = diaryentry.count_words()
    assert result == 3

def test_number_of_words_in_contents_two():
    diaryentry = DiaryEntry("Mandalorian", "an iconic sci-fi great")
    result = diaryentry.count_words()
    assert result == 4

"""
Given a rate of wpm 
It returns the estimate reading time in minutes of contents
"""

def test_estimate_reading_time_for_ten_wpm():
    diaryentry = DiaryEntry("Mandalorian", "a sci-fi great")
    result = diaryentry.reading_time(10)
    assert result == 1

def test_estimate_reading_time_for_five_wpm():
    diaryentry = DiaryEntry("Mandalorian", "a great sci-fi movie with action")
    result = diaryentry.reading_time(5)
    assert result == 2

def test_estimate_reading_time_for_0_wpm():
    diaryentry = DiaryEntry("Mandalorian", "a great sci-fi movie with action")
    with pytest.raises(Exception) as e:
        diaryentry.reading_time(0)
    error_message = str(e.value)
    assert error_message == "Cannot estimate reading time with 0 wpm"



"""
Given a contents, rate of wpm and minutes to read
It returns number of words the user can read
"""

def test_estimate_number_of_words_user_can_read_given_a_limit():
    diaryentry = DiaryEntry("Mandalorian", "a great sci-fi movie with action")
    result = diaryentry.reading_chunk(3, 1)
    assert result == "a great sci-fi"


def test_estimate_number_of_words_user_can_read_given_a_limit():
    diaryentry = DiaryEntry("Mandalorian", "a great sci-fi movie with action")
    diaryentry.reading_chunk(3, 1)
    result = diaryentry.reading_chunk(3, 1)
    assert result == "movie with action"