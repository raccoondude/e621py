# epy

[![epy](https://i.imgur.com/DOqumRI.jpg "epy")](https://i.imgur.com/DOqumRI.jpg "epy")
A e621 API wrapper for python!


###Current status

Beta

###documentation

**Installation**

run: `pip3 install e621py`

**Importing library**

`import e621py`

**Users**

    #import library
    from e621py import User
    #add the user
    user = User("YOURUSERNAME", "YOUR API KEY (or just a empty string)")
    #recive the api key, once you run this function the user object will update the API_Key field
    Key = user.GetKey("YOURPASSWORD")
    print("Key") #Will return the key
    print(user.API_Key) #Will return the new key
    

**Posts**

    from e621py import Post
    post = Post("POST ID")
    
    jsonout = post.GetData() #Returns JSON output
    
    strout = post.GetDataString() #Returns JSON output as string

##Notice

By using this module, you agree to E621s ToS, and you are willing to view sesitive content (NSFW/L)

I am NOT responsible for any actions done with this module

##Credit

Everything was done by me

The little logo was done by [Vorskul](https://instagram.com/voskul "Vorskul")
