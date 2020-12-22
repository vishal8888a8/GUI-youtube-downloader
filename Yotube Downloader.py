from pytube import YouTube
from tkinter import *


#main download part
def download(link):
    obj = YouTube(link)
    dl = obj.streams.get_highest_resolution()
    print("Downloading in proccess")
    dl.download()
    print("Downloading completed!")

#getting the link as string
def get_class():
    link=ent.get()
    download(link)

#window properties
window = Tk()
window.geometry("573x400")
window.title("YouTube Downloader")
window.configure(background="#e0db31")

#logo set-up
logo = PhotoImage(file="logo.png")
l1 = Label(window,image=logo,bg="#962383",anchor="center").pack()

#second label
l2=Label(window,text="Enter Your link below!",font="times 20 bold",bg="#4640e6")
l2.pack(pady=15,padx=10)

#taking input from the user
ent = Entry(window,textvariable = StringVar)
ent.pack(padx=10, pady=14)

#the enter button
btn1 = Button(window, text="Click Me!", command=get_class)
btn1.pack(padx=10, pady=13)

#output
T = Text(window, height = 5, width = 52)

#end of the window loop
window.mainloop()
