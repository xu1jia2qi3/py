from tkinter import *
import json
import os
import sys


window = Tk()
window.minsize(600,450)
window.title("Welcome to LikeGeeks app")
data = {}

config_name = 'config.json'
#this is how pyinstaller use relative path
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)
config_path = os.path.join(application_path, config_name)


try:
    with open(os.path.join( config_path) , 'r') as f:
        data = json.load(f)
    
except Exception as E:
    print('oops!', E)
    print('looking in', config_path)



lbl = Label(window, text=data["a"])

lbl.grid(column=0, row=0)

window.mainloop()