#Python Verson 3.9.0

#Author: Forest Moher

#Purpose: Student tracking application using Tkinter

#Written and tested on Win10

from tkinter import *
import tkinter as tk

import studentTracker_gui
import studentTracker_func

class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):

        #define our master frame configuration
        self.master = master
        self.master.minsize(300,600) #(height,width)
        self.master.maxsize(300,600)
        #This CenterWindow method will center our app on the users screen
        #studentTracker_func.center_window(self,300,600)
        self.master.title("Student Tracker")
        self.master.configure(bg="#f0f0f0")
        #the protocol method is a tkinter built in method to catch if
        #the user clicks the upper corner X on the windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: studentTracker_func.ask_quit(self))
        arg = self.master

        # load in the gui widgets from a seperate module,
        # keeping your code compartmentalized and clutter free
        studentTracker_gui.load_gui(self)


if __name__ =="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
