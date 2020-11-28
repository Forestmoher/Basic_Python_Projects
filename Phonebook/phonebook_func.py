
import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3

#import other modules
import phonebook_main
import phonebook_gui



def center_window(self,w,h): #pass the tkinter frame (master) reference and the w and h
    #get user's screen w and h
    screen_width = self.master.winfo_screenwidth()#this grabs the users window height and width
    screen_height = self.master.winfo_screenheight()
    #calculate x and y coordinates to paint the app center on the screen
    x = int((screen_width/2)-(w/2))
    y = int((screen_height/2)-(h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo


#catch if the user clicks on the windows upper-right 'x' to ensure that they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit Program","Okay to exit application?"):
        #This closes the app
        self.master.destroy()
        os._exit(0)#this will release all the memory used by building this app.


#=============================================================
def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        # You must commit()to save the changes and close the db connection
        conn.commit()
    conn.close()
    first_run(self)


def first_run(self):
    data = ('John','Doe','John Doe','111-111-1111','jdoe@gmail.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(data))
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur,count


#Select item in ListBox
def onSelect(self,event):
    #calling the event is the self.lstList1 widget
    varList = event.widget
    select  = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        #This returns a tuple and we can slice in into 4 parts using the data[] diring the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])


def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    #normalize the data to keep it consistent with the dB
    var_fname = var_fname.strip() #This will remove any blank spaces before and after each user entry
    var_lname = var_lname.strip() #This will ensure that the first character in each word is capitalized
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname))
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email:
        print("Incorrect email format")
    if (len(var_fname)>0) and (len(var_lname)>0) and (len(var_phone)>0) and (len(var_email)>0):
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.cursor()
            #Check the data base for the existence of a full name, if so we will alert the user and disregard the request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # if this is 0, then there is no existence of a full name and we can add new data
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook(col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email))
                self.lstList1.insert(END, var_fullname)#update lstbox with the new fullname
                onClear(self) #call the function to clear all the text boxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database. Please choose a different name.".format(var_fullname))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing text Error","Please ensure that there is data entered in all four fields.")



def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) #listbox's selected value
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        #check  count to ensure that this is not the last record is
        #the dB...cannot delete last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation","All information associated with ({}) \nwill be permnently deleted \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self)#call the function to clear all of the text boxes and the selected index of listbox
                onRefresh(self) #update the listbox of the changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record error","({}) is the last record in the database and connot be deleted at this time".format(var_select))
    conn.close()


def onDeleted(self):
    #clear the text in the textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    onRefresh(self) #update the listbox of the changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    #clear the text in the text boxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)


def onRefresh(self):
    #populate the list boxes coinciding with the dB
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        i = 0
        while i < count:
            cur.execute("""SElECT col_fullname FROM tbl_phonebook""")
            varList = cur.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i += 1
    conn.close()


def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0]#index of the list selection
        var_value = self.lstList1.get(var_select)#list selections text value
    except:
        messagebox.showinfo("Missiing Selection","No name was selected from the list box \nCancelling the update request.")
        return
    #the user will only be allowed to update changes for the phone and emails
    #for name changes, the user will need to delete and re enter the the entire record
    var_phone = self.txt_phone.get().strip() #normalizes the data too maintain dB integrity
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0): #ensure that there is data present
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            #count the records to see if the user's changes are already in
            # the dB...meaning, there are no changes to update.
            cur.execute("""SElECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SElECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            if count == 0 or count2 == 0: # if proposed changes are not alreadt in the dB, then proceed
                response = messagebox.askokcancel("Update Request","The following changes ({}) and ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_phone,var_email,var_value))
                print(response)
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{0}',col_email = '{}' WHERE col_fullname = '{2}'""".format(var_phone,var_email,var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel Request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No Changes Detected","Both ({}) and ({}) \nalready  exist in the database for this name. \n\n Your update request has been cancelled.".format(var_phone,var_email))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing Infomation","Please select a name from the list. \nThen edit the phone and email information.")
    onClear(self)
                    

if __name__ == "__main__":
    pass

    
