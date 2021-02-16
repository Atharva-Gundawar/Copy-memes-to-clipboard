import requests 
import json
from PIL import Image
import os 
from io import BytesIO
import win32clipboard
from PIL import Image

def getmemes(genre = "memes"):
    url = "https://meme-api.herokuapp.com/gimme/" + genre

    r = requests.get(url)
    json_response = r.json()
    url = json_response['url']

    print(url)
    urlList= list(url)
    if urlList[-3:] == "gif":
        print("found gif")
        getmemes()
    else:
        im = Image.open(requests.get(json_response['url'], stream=True).raw)
        im.show()
