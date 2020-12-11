from tkinter import *
import tkinter as tk

import studentTracker_main
import studentTracker_func

def load_gui(self):

    self.lbl_fname = tk.Label(self.master,text='First Name:')
    self.lbl_fname.grid(row=0,column=1,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_lname = tk.Label(self.master,text='Last Name:')
    self.lbl_lname.grid(row=2,column=1,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_grade = tk.Label(self.master,text='Grade Level:')
    self.lbl_grade.grid(row=4,column=1,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_id = tk.Label(self.master,text='Student ID:')
    self.lbl_id.grid(row=6,column=1,padx=(27,0),pady=(10,0),sticky=N+W)

    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=1,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+W)
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=3,column=1,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+W)
    self.txt_grade = tk.Entry(self.master,text='')
    self.txt_grade.grid(row=5,column=1,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+W)
    self.txt_id = tk.Entry(self.master,text='')
    self.txt_id.grid(row=7,column=1,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+W)

    #Define the list box with a scrollbar
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>',lambda event: studentTracker_func.onSelect(self,event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=15,column=5,rowspan=4,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.lstList1.grid(row=15,column=1,rowspan=4,columnspan=4,padx=(0,0),pady=(0,0))#sticky=N+E+S+W)

    self.btn_add = tk.Button(self.master,width=6,height=1,text='Add',command=lambda: studentTracker_func.addToList(self))
    self.btn_add.grid(row=1,column=4,padx=(0,0),pady=(10,0),sticky=E)
    self.btn_update = tk.Button(self.master,width=6,height=1,text='Upate',command=lambda: studentTracker_func.onUpdate(self))
    self.btn_update.grid(row=2,column=4,padx=(0,0),pady=(10,0),sticky=E)
    self.btn_delete = tk.Button(self.master,width=6,height=1,text='Delete',command=lambda: studentTracker_func.onDelete(self))
    self.btn_delete.grid(row=3,column=4,padx=(0,0),pady=(10,0),sticky=E)
    self.btn_close = tk.Button(self.master,width=6,height=1,text='Close',command=lambda: studentTracker_func.ask_quit(self))
    self.btn_close.grid(row=4,column=4,columnspan=1,padx=(0,0),pady=(10,0),sticky=E)

    phonebook_func.create_db(self)
    phonebook_func.onRefresh(self)


if __name__ == "__main__":
    pass
