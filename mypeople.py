from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import datetime
from PIL import ImageTk,Image
from addpeople import AddPeople
from updatepeople import Update
from displaypeople import DisplayPeople

con = sqlite3.connect('contacts.db')
cur = con.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("600x600+600+50")
        self.title("My People")
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

        self.heading = Label(self.top, text='My People', font='arial 15 bold', bg='white', fg='#34bab2')
        self.heading.place(x=260, y=65)

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)

        self.listbox = Listbox(self.bottom, width=45, height=27, font='arial 10 bold', fg='#34bab2')
        self.listbox.grid(row=0, column=0, padx=(40,0))
        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)

        persons = cur.execute("SELECT * FROM 'addressbook'").fetchall()
        count = 0
        for person in persons:
            self.listbox.insert(count, str(person[0])+ ". " +person[1]+ " " +person[2])
            count+=1

        self.scroll.grid(row=0, column=1, sticky=N+S)


        #buttons

        btnadd = Button(self.bottom, text="Add", width=12, font="Sans 12 bold", command=self.add_people)
        btnadd.grid(row=0, column=2, padx=40, pady=30, sticky=N)

        btnUpdate = Button(self.bottom, text="Update", width=12, font="Sans 12 bold", command=self.update_person)
        btnUpdate.grid(row=0, column=2, padx=40, pady=90, sticky=N)

        btnDisplay = Button(self.bottom, text="Display", width=12, font="Sans 12 bold", command=self.display_person)
        btnDisplay.grid(row=0, column=2, padx=40, pady=150, sticky=N)

        btnDelete = Button(self.bottom, text="Delete", width=12, font="Sans 12 bold", command=self.delete_person)
        btnDelete.grid(row=0, column=2, padx=40, pady=210, sticky=N)


    def add_people(self):
        add_page = AddPeople()
        self.destroy()

    def update_person(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]
        
        update_page = Update(person_id)
        self.destroy()

    def display_person(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        display_page = DisplayPeople(person_id)
        self.destroy()

    def delete_person(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        query = "DELETE FROM 'addressbook' WHERE person_id = '{}'".format(person_id)
        str_for_mbox = "Are you sure you want to delete "+person.split(".")[1]+"?"
        answer = messagebox.askquestion("Warning", str_for_mbox)
        if answer == 'yes':
            try:
                cur.execute(query)
                con.commit()
                ans = messagebox.showinfo("Success","Contact Deleted Successfully")
                if ans == 'ok':
                    self.destroy()
                    person = MyPeople()

            except:
                messagebox.showinfo("Error","Sorry! Unable to delete contact.")