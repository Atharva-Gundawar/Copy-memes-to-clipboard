from PIL import Image
import logging
import requests 
import json
import os 

logging.basicConfig(filename='posts.log',format='%(message)s',
                    level=logging.ERROR)

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
        title = json_response['title']
        url = json_response['url']
        im = Image.open(requests.get(url, stream=True).raw)
        logging.error('%s => %s', title, url)
        im.show()
