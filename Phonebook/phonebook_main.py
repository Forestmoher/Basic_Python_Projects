#Python Verson 3.9.0

#Author: Forest Moher

#Purpose: Phonebook application built using the Tkinter module

#Written and tested on Win10

from tkinter import *
import tkinter as tk

import phonebook_gui
import phonebook_func

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):

        #define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(height,width)
        self.master.maxsize(500,300)
        #This CenterWindow method will center our app on the users screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#f0f0f0")
        #the protocol method is a tkinter built in method to catch if
        #the user clicks the upper corner X on the windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the gui widgets from a seperate module,
        # keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)






if __name__ =="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

