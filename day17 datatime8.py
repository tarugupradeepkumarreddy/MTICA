from tkinter import *
master=Tk()
demo_text="This is a sample demo of message widger."
msg=message(master, text=demo_text)
msg.config(bg='lightgreen', font=('times',24,'italic'))

msg.pack()
##w=Label(root,text="Hello Pradeep")
##w.pack()
##root.mainloop()
