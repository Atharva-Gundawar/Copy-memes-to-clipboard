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



def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()
    print("copied")


# if __name__ == "__main__":
#     main()