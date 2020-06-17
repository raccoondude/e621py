# e621py

BROKEN, e621py is outdated and will no longer work

[![e621py](https://i.imgur.com/DOqumRI.jpg "e621py")](https://i.imgur.com/DOqumRI.jpg "e621py")
A e621 API wrapper for python!


### Current status

Release 1.00

### documentation

## USE THIS

My code is shit, i mean, it works, but it's shit.

So, if you want to edit the source code, use this [fork](https://github.com/superwhiskers/e621py "fork")

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
    
    Results = Query.Tag("male/male+cuddling+rating:s") #returns a string of text
    Results = json.loads(Results)
    
    URL = Results[0]['file_url'] #first [] defines whitch out of the set to pick from, the second is for the json query
    
    Query.Show(URL) #Shows image from url
    Query.Save(URL) #Saves image from url


### Notice

I am NOT responsible for any actions done with this module

If there is an issue, I cannot stop it, please don't bother me

### Credit

Everything was done by me

The little logo was done by Vorskul

Used [downloader-cli](https://github.com/deepjyoti30/downloader-cli "downloader-cli") please go show him some love!
