class Musictracker():
    def __init__(self):
        self.track_list = []

    def add(self, track):
        self.track_list.append(track)

    def tracks_listened_to(self):
        if self.track_list == []:
            raise Exception("Track list empty")
        else:
            return self.track_list
    