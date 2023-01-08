from tkinter import *
class App:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()
        self.button=Button(frame,text="Quit",fg="red",command=quit)
        self.button.pack(side=LEFT)
        self.slogan=Button(frame,text="hell",
                           command=self.write_slogan)
        self.slogan.pack(side=LEFT)
    def write_slogan(self):
        print("pradeepkumarreddy")
root=Tk()
app=App(root)
