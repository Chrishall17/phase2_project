Exercise:
1. Describe the Problem
As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

2. Design the Class System
    # DiaryEntry                        -----       #Todos
    #                                               #
    # - entries                                     # - task
    # - todo list                                   # - complete as false
    # - contact list                                # - mark complete as true
    # - add(experience + contact)                   #
    # - add(tasks)                                  #
    #                                               #

    |
    |
    |

    # Experiences
    #
    # - name
    # - entry
    # - contact
    # - date


Class DiaryTracker()
    # User facing properties:
    #   tracks: a dictionary of diary entries
    #   tracks: a list of tasks to do \

    def __init__(self):
        pass # No code here yet

    def add_entry(self, experience):
        # Parameters:
            #   track: an instance of experience
            # Side-effects:
            #   Adds the experience to the diary property of the self object
            pass # No code here yet

    def add_task(self, task):
        # Parameters:
            #   track: an instance of task
            # Side-effects:
            #   Adds the experience to the task list property of the self object
            pass # No code here yet

    def task_list(self):
        #Parameters:
            #   return: a list of tasks todo
            # Side-effects:
            #   none
            pass # No code here yet

    def read_entry(self, date):
        #Parameters:
                #   return: entry contents given from a specific date
                # Side-effects:
                #   throws error if no diary entry on that date
                pass # No code here yet

{{PROBLEM}} Multi-Class Planned Design Recipe
1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

2. Design the Class System
Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com

┌────────────────────────────┐
│ MusicPlayer                │
│                            │
│ - tracks                   │
│ - add(track)               │
│ - search_by_title(keyword) │
│   => [tracks...]           │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Track(title, artist)    │
│                         │
│ - title                 │
│ - artist                │
│ - format()              │
│   => "TITLE by ARTIST"  │
└─────────────────────────┘
Also design the interface of each class in more detail.

class MusicLibrary:
    # User-facing properties:
    #   tracks: list of instances of Track

    def __init__(self):
        pass # No code here yet

    def add(self, track):
        # Parameters:
        #   track: an instance of Track
        # Side-effects:
        #   Adds the track to the tracks property of the self object
        pass # No code here yet

    def search_by_title(self, keyword):
        # Parameters:
        #   keyword: string
        # Returns:
        #   A list of the Track objects that have titles that include the keyword
        pass # No code here yet


class Track:
    # User-facing properties:
    #   title: string
    #   artist: string

    def __init__(self, title, artist):
        # Parameters:
        #   title: string
        #   artist: string
        # Side-effects:
        #   Sets the title and artist properties
        pass # No code here yet

    def format(self):
        # Returns:
        #   A string of the form "TITLE by ARTIST"
        pass # No code here yet
3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
Encode each example as a test. You can add to the above list as you go.

5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.