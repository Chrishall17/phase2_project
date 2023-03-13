import pytest 
from lib.music_tracker import Musictracker

"""
When we add a track
It is reflected in the list
"""
def test_add_track_reflected_in_list_of_tracks():
    musictracker = Musictracker()
    musictracker.add("Eye of the tiger")
    assert musictracker.tracks_listened_to() == ["Eye of the tiger"]

"""
When we add multiple tracks
They are reflected in the list
"""
def test_add_multiple_track_reflected_in_list_of_tracks():
    musictracker = Musictracker()
    musictracker.add("Eye of the tiger")
    musictracker.add("Final countdown")
    musictracker.add("Happy") 
    result = musictracker.tracks_listened_to() 
    assert result == ["Eye of the tiger", "Final countdown", "Happy"]

"""
When we dont add any tracks
Calling the tracker returns an error => "Track list empty"
"""
def test_track_list_empty_throws_an_error():
    musictracker = Musictracker()
    with pytest.raises(Exception) as e:
        musictracker.tracks_listened_to()
    error_message = str(e.value)
    assert error_message == "Track list empty"