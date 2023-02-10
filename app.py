import tkinter as tk

import time
import pystray
from tkinter import *
from tkinter import messagebox
from PIL import Image
import AppKit

class Gui():

    def __init__(self):
        self.window = tk.Tk()

        self.darwin_nsapplication = AppKit.NSApplication.sharedApplication()
        self.image = Image.open("./images/noname.png")
        self.menu = (
            pystray.MenuItem('Show', self.show_window),
            pystray.MenuItem('Quit', self.quit_window)
            )
        
    # Declaration of variables
        self.hour=StringVar()
        self.minute=StringVar()
        self.second=StringVar()
    
        # setting the default value as 0
        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")
    
    # Use of Entry class to take input from the user
        hourEntry= Entry(self.window, width=3, font=("Arial",18,""),
                        textvariable=self.hour)
        hourEntry.place(x=80,y=20)
        
        minuteEntry= Entry(self.window, width=3, font=("Arial",18,""),
                        textvariable=self.minute)
        minuteEntry.place(x=130,y=20)
        
        secondEntry= Entry(self.window, width=3, font=("Arial",18,""),
                        textvariable=self.second)
        secondEntry.place(x=180,y=20)
        # button widget
        btn = Button(self.window, text='Set Time Countdown', bd='5',
                    command= self.submit)
        btn.place(x = 70,y = 120)
    
    def submit(self):
        try:
            # the input provided by the user is
            # stored in here :temp
            temp = int(self.hour.get())*3600 + int(self.minute.get())*60 + int(self.second.get())
        except:
            print("Please input the right value")
        while temp >-1:
            
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60)
    
            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours=0
            if mins >60:
                
                # divmod(firstvalue = temp//60, secondvalue
                # = temp%60)
                hours, mins = divmod(mins, 60)
            
            # using format () method to store the value up to
            # two decimal places
            self.hour.set("{0:2d}".format(hours))
            self.minute.set("{0:2d}".format(mins))
            self.second.set("{0:2d}".format(secs))
    
            # updating the GUI window after decrementing the
            # temp value every time
            self.window.update()
            time.sleep(1)
    
            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")
            
            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1
    
    

    def quit_window(self):
        self.icon.stop()
        self.window.destroy()


    def show_window(self):
        self.icon.stop()
        self.window.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        self.window.after(0, self.window.deiconify)


    def withdraw_window(self):
        self.window.withdraw()
        self.icon = pystray.Icon("name", self.image, "title", self.menu)
        self.icon.run_detached()


if __name__ in '__main__':
    app = Gui()
    app.window.protocol('WM_DELETE_WINDOW', app.withdraw_window)
    app.window.mainloop()