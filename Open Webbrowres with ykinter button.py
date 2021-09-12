# Create application to open a website
from tkinter import *
import webbrowser
parentwindow =Tk()
parentwindow.geometry('450x300')
parentwindow.title("Webbrowser")
app_name=Label(parentwindow,text='Text to Speach Application',bg='yellow',fg='red',font='Arial 16 bold')
app_name.place(x=80,y=20)
def open():
    webbrowser.open("https://voicemaker.in/")

button1 =Button(parentwindow,width=20,font=('arial 16 bold'),bg='orange',text="VoiceMaker",command=open)
button1.place(x=90,y=100)
parentwindow.mainloop()