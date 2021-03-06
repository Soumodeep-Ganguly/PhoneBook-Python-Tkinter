from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import datetime
from PIL import ImageTk,Image

con = sqlite3.connect('contacts.db')
cur = con.cursor()

class Update(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)

        self.geometry("600x600+600+50")
        self.title("Update Exixting Person")
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

        self.heading = Label(self.top, text='Update Existing Person', font='arial 15 bold', bg='white', fg='#34bab2')
        self.heading.place(x=260, y=65)

        query = "SELECT * FROM 'addressbook' WHERE person_id = '{}'".format(person_id)
        result = cur.execute(query).fetchone()
        self.person_id = person_id

        #name
        self.label_name = Label(self.bottom, text="Name", font='arial 13 bold', bg='#34bab2', fg='white')
        self.label_name.place(x=40, y=40)

        self.entry_name = Entry(self.bottom, width=40,bd=1)
        self.entry_name.insert(0, result[1])
        self.entry_name.place(x=200, y=40)

        #surname
        self.label_surname = Label(self.bottom, text="SurName", font='arial 13 bold', bg='#34bab2', fg='white')
        self.label_surname.place(x=40, y=80)

        self.entry_surname = Entry(self.bottom, width=40,bd=1)
        self.entry_surname.insert(0,result[2])
        self.entry_surname.place(x=200, y=80)

        #email
        self.label_email = Label(self.bottom, text="Email", font='arial 13 bold', bg='#34bab2', fg='white')
        self.label_email.place(x=40, y=120)

        self.entry_email = Entry(self.bottom, width=40,bd=1)
        self.entry_email.insert(0,result[3])
        self.entry_email.place(x=200, y=120)

        #phone_number
        self.label_phn = Label(self.bottom, text="Phone Number", font='arial 13 bold', bg='#34bab2', fg='white')
        self.label_phn.place(x=40, y=160)

        self.entry_phn = Entry(self.bottom, width=40,bd=1)
        self.entry_phn.insert(0,result[4])
        self.entry_phn.place(x=200, y=160)

        #address
        self.label_addr = Label(self.bottom, text="Address", font='arial 13 bold', bg='#34bab2', fg='white')
        self.label_addr.place(x=40, y=200)

        self.entry_addr = Text(self.bottom, width=30, height=8)
        self.entry_addr.insert(1.0,result[5])
        self.entry_addr.place(x=200, y=200)

        #button
        button = Button(self.bottom, text="Update Person", font='arial 15 bold', bg='white', fg='#34bab2', command=self.update_people)
        button.place(x=170, y=370)

    
    def update_people(self):
        person_id = self.person_id
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phn.get()
        address = self.entry_addr.get(1.0,'end-1c')

        if name and surname and email and phone and address != "":
            try:
                #add to the database
                query = "UPDATE 'addressbook' SET person_name=?,person_surname=?,person_email=?,person_phone=?,person_address=? WHERE person_id=?"
                cur.execute(query, (name,surname,email,phone,address,person_id))
                con.commit()
                self.destroy()
                messagebox.showinfo("Success","Contact Updated Successfully.")                
            except:
                messagebox.showerror("Error", "Sorry!There was an unexpected error.")
        else:
            messagebox.showerror("Error", "Don't Leave any field empty.", icon='warning')