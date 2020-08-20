from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
from mypeople import MyPeople
from addpeople import AddPeople
from aboutus import About

date = datetime.now().date()
date = str(date)

class Application(object):
    def __init__(self, master):
        self.master = master

        # frames

        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg='#34bab2')
        self.bottom.pack(fill=X)

        #top frame design
        self.top_image = ImageTk.PhotoImage(Image.open('icons/phonebook.png'))
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=120, y=50)

        self.heading = Label(self.top, text='My PhoneBook App', font='arial 15 bold', bg='white', fg='#34bab2')
        self.heading.place(x=260, y=65)

        self.date_lbl = Label(self.top, text="Today's Date: "+date, font='arial 10 bold', bg='white',fg='#34bab2')
        self.date_lbl.place(x=470, y=120)

        #button - view people
        self.viewButton = Button(self.bottom, text='View People', width=12, font='arial 12 bold', bg='white',fg='#34bab2', command=self.my_people)
        self.viewButton.place(x=250, y=100)

        #button - add people
        self.addButton = Button(self.bottom, text='Add People', width=12, font='arial 12 bold', bg='white',fg='#34bab2', command=self.add_people)
        self.addButton.place(x=250, y=160)

        #button - about us
        self.aboutButton = Button(self.bottom, text='About Us', width=12, font='arial 12 bold', bg='white',fg='#34bab2', command=self.about_us)
        self.aboutButton.place(x=250, y=220)

    def my_people(self):
        people = MyPeople()

    def add_people(self):
        add_page = AddPeople()

    def about_us(self):
        about_page = About()


def main():
    root = Tk()
    app = Application(root)
    root.title("PhoneBook App")
    root.geometry("650x550+350+100")
    root.resizable(False,False)
    root.mainloop()


if __name__ == '__main__':
    main()