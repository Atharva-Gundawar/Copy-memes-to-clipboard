from helper import getPosts
import keyboard
import time

getMemeShortcut = "ctrl + m"
endScript = "ctrl + c"

while True:
    if keyboard.is_pressed(getMemeShortcut):
        getPosts("meme")
        time.sleep(0.5)
    elif keyboard.is_pressed(endScript):
        break
    time.sleep(0.01)