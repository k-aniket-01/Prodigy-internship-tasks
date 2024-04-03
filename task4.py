import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime

def on_press(key):
    if key == Key.space or key == Key.enter:
        with open("keystrokes.txt", "a") as f:
            f.write(f"{datetime.now()} - {key}\n")

def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()