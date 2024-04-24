print("Question No 3")

class Music_libreary_system:
    def __init__(self):
        return
    
class Song(Music_libreary_system):
    def __init__(self,title,artist,album,duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration



class Playlist(Music_libreary_system):
    def __init__(self,title,discription,listsongs):
        super().__init__()
        self.title = title
        self.discription = discription
        self.listsongs = listsongs

class Library(Music_libreary_system):
    def __init__(self,listofplaylist):
        super().__init__()
        self.listofplaylist = listofplaylist


songs = Song("dil","Atif","Aashqui2",50)
print(songs.title,songs.artist,songs.album,songs.duration)


playlist = Playlist("Ali","Nothing",["Awara"])
print(playlist.title,playlist.discription,playlist.listsongs)

lib = Library(["Romantic","Sad"])
print(lib.listofplaylist)

    

