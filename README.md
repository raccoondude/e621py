# epy

[![epy](https://i.imgur.com/DOqumRI.jpg "epy")](https://i.imgur.com/DOqumRI.jpg "epy")
A e621 API wrapper for python!


### Current status

Beta Devloping (0.12)

### documentation

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
    objectvar  = post.MakePostData() #returns data object
    strout = post.GetDataString() #Returns JSON output as string
	NSFW = post.isNSFW() #returns true or false
	post.Show() #returns image in imagick
	Rate = post.GetRating() #returns rating
	File = post.GetFileURL() #return file url
    

**Query**

    import e621py
    import json
    
    Query = e621py.Query()
    
    Results = Query.Tag("male/male+cuddling") #returns a string of text
    Results = json.loads(Results)
    
    URL = Results[0]['file_url'] #first [] defines whitch out of the set to pick from, the second is for the json query
    
    Query.Show(URL) #Shows image from url
    Query.Save(URL) #Saves image from url


### Notice

By using this module, you agree to E621s ToS, and you are willing to view sesitive content (NSFW/L)

I am NOT responsible for any actions done with this module

### Credit

Everything was done by me

The little logo was done by [Vorskul](https://instagram.com/voskul "Vorskul")
