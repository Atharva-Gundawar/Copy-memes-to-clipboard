from PIL import Image
import requests 
import json
import os 

def getPosts(genre = "memes"):

    url = "https://meme-api.herokuapp.com/gimme/" + genre

    r = requests.get(url)
    json_response = r.json()
    url = json_response['url']

    print(url)
    urlList= list(url)
    if urlList[-3:] == "gif":
        pass
    else:
        im = Image.open(requests.get(json_response['url'], stream=True).raw)
        im.show()