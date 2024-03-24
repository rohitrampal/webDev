from tkinter import *
from pytube import YouTube  
# pip install pytube
a=Tk()
a.geometry("1000x700")                    #size of whole screen
a.config(bg="black")                      # bacground color
a.title("Video downloder")

Label(a,text="YouTube",font=("Arial",49,"bold"),bg="red").pack()

Label(a,text="Videodnd",font=("Arial",25,"bold"),bg="red").pack()

link= StringVar()
Label(a,text="Enter the link ",font=("Arial",29,"bold")).place(x=400,y=150)

E_link= Entry(a,width=50,font=35,textvariable=link, bd=10).place(x=300,y=200)

def fun1():
    url=YouTube(str(link.get()))
    v=url.streams.first()
    v.download()
    Label(a,text="Downloading completed !!",font=("Arial",26,"bold"),bg="yellow").place(x=150,y=400)
    Label(a,text="Check the respective python project folder",font=("Arial",26,"bold"),bg="yellow").place(x=150,y=550)

Button(a,text="DOWNLOAD",font=("Arial",29,"bold"),bg="light green",command=fun1).place(x=350,y=300)


a.mainloop()