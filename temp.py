from pynput.keyboard import Key, Listener
import sys
from copymemetoclipboard import getmemes

def on_press(key):
    # print('{0} pressed'.format(key))
    keylist = list(str(key))
    if keylist[2] == "r":
        print("this is meme shortcut")
        getmemes("nsfw")
    # if keylist[2] == "x" and keylist[3] == "0" and keylist[4] == "2" :  
    #     print(key)
    #     sys.exit("Byeee")
def on_release(key):
    # print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()