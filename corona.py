import requests
import bs4

import tkinter as tk

def htmldata(url):
    data=requests.get(url)
    return data

def coviddata():
    url="https://www.worldometers.info/coronavirus/"
    getdata=htmldata(url)
    bs=bs4.BeautifulSoup(getdata.text, 'html.parser')
    info=bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    
    # print(info)
    alldata=""

    for block in info:
        text=block.find("h1", class=None).get_text()

        count=block.find("span", class=None).get_text()
        
           
        alldata=alldata + text + " " + count + "\n"

        
    return alldata


def reload():
    newdata= coviddata()
    mainlabel['text']=newdata



def search():
    name=textfield.get()

    url="https://www.worldometers.info/coronavirus/country/"+ name
    getdata=htmldata(url)
    bs=bs4.BeautifulSoup(getdata.text, 'html.parser')
    info=bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
            
    # print(info)
    alldata=""

    for block in info:
        text=block.find("h1", class=None).get_text()

        count=block.find("span", class=None).get_text()
        
       
        alldata=alldata + text + " " + count + "\n"

        
    mainlabel['text']=alldata





coviddata()

root=tk.Tk()
root.geometry("600x600")
root.title("Corona Virus Detail")
f=("arieal", 25,"bold")

# banner= tk.PhotoImage(file="svg.png")
# bannerlabel= tk.Label(root, image=banner)
# bannerlabel.pack()

textfield= tk.Entry(root, width=50)
textfield.pack()

mainlabel=tk.Label(root, text=coviddata(), font=f).pack()


sbtn=tk.Button(root ,text="Search", font=f ,relief='solid', command=search)
sbtn.pack()




rbtn=tk.Button(root ,text="Reload", font=f ,relief='solid', command=reload)
rbtn.pack()




root.mainloop()