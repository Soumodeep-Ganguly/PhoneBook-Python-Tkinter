from tkinter import *

class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("500x400+400+50")
        self.title("About Us")
        self.resizable(False,False)

        # frames

        self.top = Frame(self, height=400, width=500, bg='#34bab2')
        self.top.pack(fill=BOTH)

        self.heading = Label(self.top, text='Hey this is about us page'
                            '\n this application is made to store contacts'
                            '\n you can contact us on'
                            '\n Facebook'
                            '\n LinkedIn'
                            '\n Youtube'
                            '\n\n\n\n\n Thank You',
                            font='arial 15 bold', bg='#34bab2', fg='white'
                            )
        self.heading.place(x=50, y=50)