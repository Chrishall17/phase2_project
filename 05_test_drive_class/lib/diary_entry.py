class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        count = len(self.contents.split())
        return count

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Cannot estimate reading time with 0 wpm")
        estimate_time = (len(self.contents.split()) / wpm) + 0.5
        return round(estimate_time)

    def reading_chunk(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        words = self.contents_words()
        if self.read_so_far >= len(words):
            self.read_so_far = 0
            
        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + words_user_can_read
        chunk_words = words[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return " ".join(chunk_words)
    
    def contents_words(self):
        return self.contents.split()

        


        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
    

diaryentry = DiaryEntry("Mandalorian", "a great sci-fi movie with action 1 2 3")
print(diaryentry.reading_chunk(3, 1))
print(diaryentry.reading_chunk(3, 1))

