from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('800x600')

root.title("YouTube Downloader")


label=Label(root,text = 'youtub donlloader', font ='arial 20 bold')
label.pack()





link = StringVar()

linkLabel=Label(root, text = 'paste ur link:', font = 'arial 15 bold')
linkLabel.pack()

linkentry = Entry(root, width = 70,textvariable = link)
linkentry.pack()







def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    donLabel=Label(root, text = 'donlod', font = 'arial 15')
    donLabel.pack()


donbtn=Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,command = Downloader)
donbtn.pack()




root.mainloop()
