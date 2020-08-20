from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import datetime
from PIL import ImageTk,Image

con = sqlite3.connect('contacts.db')
cur = con.cursor()

class DisplayPeople(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)

        self.geometry("600x600+600+50")
        self.title("Person Details")
        self.resizable(False,False)

        # frames

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#34bab2')
        self.bottom.pack(fill=X)

        #top frame design
        self.top_image = ImageTk.PhotoImage(Image.open('icons/phonebook.png'))
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=120, y=50)

        self.heading = Label(self.top, text='Person Details', font='arial 15 bold', bg='white', fg='#34bab2')
        self.heading.place(x=260, y=65)

        self.person_id = person_id
        query = "SELECT * FROM 'addressbook' WHERE person_id = '{}'".format(self.person_id)
        result = cur.execute(query).fetchone()

        #name
        self.label_name = Label(self.bottom, text="Name: ", font='arial 13 bold', bg='#34bab2', fg='white')
        self.label_name.place(x=40, y=40)

        self.entry_name = Label(self.bottom, text=result[1], font='arial 13 bold', bg='#34bab2', fg='white')
        self.entry_name.place(x=200, y=40)

        #surname
        self.label_surname = Label(self.bottom, text="SurName: ", font='arial 13 bold', bg='#34bab2', fg='white')
        self.label_surname.place(x=40, y=80)

        self.entry_surname = Label(self.bottom, text=result[2], font='arial 13 bold', bg='#34bab2', fg='white')
        self.entry_surname.place(x=200, y=80)

        #email
        self.label_email = Label(self.bottom, text="Email: ", font='arial 13 bold', bg='#34bab2', fg='white')
        self.label_email.place(x=40, y=120)

        self.entry_email = Label(self.bottom, text=result[3], font='arial 13 bold', bg='#34bab2', fg='white')
        self.entry_email.place(x=200, y=120)

        #phone_number
        self.label_phn = Label(self.bottom, text="Phone Number", font='arial 13 bold', bg='#34bab2', fg='white')
        self.label_phn.place(x=40, y=160)

        self.entry_phn = Label(self.bottom, text=result[4], font='arial 13 bold', bg='#34bab2', fg='white')
        self.entry_phn.place(x=200, y=160)

        #address
        self.label_addr = Label(self.bottom, text="Address", font='arial 13 bold', bg='#34bab2', fg='white')
        self.label_addr.place(x=40, y=200)

        self.entry_addr = Text(self.bottom, width=30, height=8, font='arial 13 bold', bg='#34bab2', fg='white', borderwidth=0)
        self.entry_addr.insert(1.0,result[5])
        self.entry_addr.config(state=DISABLED)
        self.entry_addr.place(x=200, y=200)