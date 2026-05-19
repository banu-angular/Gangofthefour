# Consider a Music Playlist. You want to be able to go through your songs one by one without needing to know if the playlist is stored as a simple list, a complex tree structure, or a remote database. The Iterator provides a standard "Next" and "HasNext" interface, allowing you to traverse the collection uniformly regardless of how it's organized.
from abc import ABC, abstractmethod
class Song:
    def __init__(self, title):
        self.title = title
class Playlist(ABC):
    @abstractmethod
    def create_iterator(self):
        pass
class SimplePlaylist(Playlist): 
    def __init__(self):
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
    def create_iterator(self):
        return SimplePlaylistIterator(self.songs)
class SimplePlaylistIterator:
    def __init__(self, songs):
        self.songs = songs
        self.position = 0
    def has_next(self):
        return self.position < len(self.songs)
    def next(self):
        if not self.has_next():
            raise StopIteration("No more songs in the playlist.")
        song = self.songs[self.position]
        self.position += 1
        return song
# Example usage
playlist = SimplePlaylist()
playlist.add_song(Song("Song 1"))
playlist.add_song(Song("Song 2"))
playlist.add_song(Song("Song 3"))
iterator = playlist.create_iterator()
while iterator.has_next():
    song = iterator.next()
    print(f"Playing: {song.title}")
    
    
# Output:
# Playing: Song 1
# Playing: Song 2
# Playing: Song 3