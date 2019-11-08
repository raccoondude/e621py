import urllib.request
import json

if __name__ == "__main__":
    pass

class User:
    def __init__(self, Username, API_Key):
        self.Username = Username
        self.API_Key = API_Key
    def GetKey(self, Password):
        parm = {
            "_client":"epy/0.0 (This is a python module by github.com/raccoondude)"
        }
        Head = {
                "User-Agent":"EPY/1.0 (A_raccoondude)"
        }
        URL = "https://e621.net/user/login.json?name="+self.Username+"&password="+Password
        uwu = urllib.request.Request(URL, headers=Head)
        owo = urllib.request.urlopen(uwu)
        owo = owo.read().decode('utf-8')
        owo = json.loads(owo)
        self.API_Key = owo['password_hash']
        return owo['password_hash']

class Post_Data:
    def __init__(self, ID, tags, file_url, artist, rating):
        self.ID = ID
        self.tags = tags
        self.file_url = file_url
        self.artist = artist
        self.rating = rating
        

    
class Post:
    def __init__(self, Post_ID):
        self.Post_ID = Post_ID
    def GetData(self):
        Head = {
                "User-Agent":"EPY/1.0 (A_raccoondude)"
        }
        URL = "https://e621.net/post/show.json?id="+self.Post_ID
        uwu = urllib.request.Request(URL, headers=Head)
        owo = urllib.request.urlopen(uwu)
        return owo
    def GetDataString(self):
        Head ={
                "User-Agent":"EPY/1.0 (A_raccoondude)"
        }
        URL = "https://e621.net/post/show.json?id="+self.Post_ID
        uwu = urllib.request.Request(URL, headers=Head)
        owo = urllib.request.urlopen(uwu)
        return owo.read()
    def GetDataJson(self):
        Head = {
                "User-Agent":"EPY/1.0 (A_raccoondude)"
        }
        URL = "https://e621.net/post/show.json?id="+self.Post_ID
        uwu = urllib.request.Request(URL, headers=Head)
        owo = urllib.request.urlopen(uwu)
        owo = owo.read()
        owo = owo.decode()
        UwU = json.loads(owo)
        return UwU
    def GetTags(self):
        Head = {
            "User-Agent":"EPY/1.0 (A_raccoondude)"
        }
        URL = "https://e621.net/post/show.json?id="+self.Post_ID
        uwu = urllib.request.Request(URL, headers=Head)
        owo = urllib.request.urlopen(uwu)
        owo = owo.read()
        owo = owo.decode()
        uwu = json.loads(owo)
        uwu = uwu['tags']
        return uwu.split(" ")
    def MakePostData(self):
        Head = {
            "User-Agent":"EPY/1.0 (A_raccoondude)"
        }
        URL = "https://e621.net/post/show.json?id="+self.Post_ID
        uwu = urllib.request.Request(URL, headers=Head)
        owo = urllib.request.urlopen(uwu)
        owo = owo.read()
        owo = owo.decode()
        UwU = json.loads(owo)
        ID = UwU['id']
        tags = UwU['tags']
        artist = UwU['artist']
        file_URL = UwU['file_url']
        rating = UwU['rating']
        OwO = Post_Data(ID, tags, artist, file_URL, rating)
        return OwO
    def GetArtist(self):
        Head = {
            "User-Agent":"EPY/1.0 (A_raccoondude)"
        }
        URL = "https://e621.net/post/show.json?id="+self.Post_ID
        uwu = urllib.request.Request(URL, headers=Head)
        owo = urllib.request.urlopen(uwu)
        owo = owo.read()
        owo = owo.decode()
        UwU = json.loads(owo)
        return UwU['artist']
    def GetFileURL(self):
        Head = {
            "User-Agent":"EPY/1.0 (A_raccoondude)"
        }
        URL = "https://e621.net/post/show.json?id="+self.Post_ID
        uwu = urllib.request.Request(URL, headers=Head)
        owo = urllib.request.urlopen(uwu)
        owo = owo.read()
        owo = owo.decode()
        UwU = json.loads(owo)
        return UwU['file_url']
    def GetRating(self):
        Head = {
            "User-Agent":"EPY/1.0 (A_raccoondude)"
        }
        URL = "https://e621.net/post/show.json?id="+self.Post_ID
        uwu = urllib.request.Request(URL, headers=Head)
        owo = urllib.request.urlopen(uwu)
        owo = owo.read()
        owo = owo.decode()
        UwU = json.loads(owo)
        return UwU['rating']
    def isNSFW(self):
        Head = {
            "User-Agent":"EPY/1.o (A_raccoondude)"
        }
        URL = "https://e621.net/post/show.json?id="+self.Post_ID
        uwu = urllib.request.Request(URL, headers=Head)
        owo = urllib.request.urlopen(uwu)
        owo = owo.read()
        owo = owo.decode()
        UwU = json.loads(owo)
        if (UwU['rating'] == 's'):
            return False
        else:
            return True
