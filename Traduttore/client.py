#!/usr/bin/python3

#-*- coding:UTF-8 -*-

import socket
from tkinter import *

def parser():
    global reply, count
    if count==1:
        window.destroy()
    count+=1
    ita=""
    eng=""
    s.connect((host, port))
    string=italianoinsert.get()+"#"+ingleseinsert.get()
    ita, eng=string.split("#")
    s.send(string.encode())
    reply=s.recv(1024).decode()
    if ita!="" and eng=="":
        ingleseinsert.insert(0, reply)
    if eng!="" and ita=="":
        italianoinsert.insert(0, reply)
    if eng!="" and ita!="":
        reply=""
        italianoinsert.delete(0, END)
        ingleseinsert.delete(0, END)
    if reply=="Non trovata":
        esito=Label(face, text="Esito: non trovata")
        esito.grid(row=1, column=3)
    else:
        esito=Label(face, text="Esito: trovata")
        esito.grid(row=1, column=3)
    s.close()

s=socket.socket()
host="127.0.0.1"
port=12555

window=Tk()
window.geometry("600x100")
window.title("Traduttore")

face=Frame(window)
face.pack()

reply=""
count=0

italiano=Label(face, text="Italiano: ")
italiano.grid(row=0, column=0)
italianoinsert=Entry(face, width="20", bg="cyan", textvariable=StringVar)
italianoinsert.grid(row=0, column=1)

inglese=Label(face, text="Inglese: ")
inglese.grid(row=0, column=2)
ingleseinsert=Entry(face, width="20", bg="cyan", textvariable=StringVar)
ingleseinsert.grid(row=0, column=3)

traduci=Button(face, text="Traduci", command=parser)
traduci.grid(row=1, column=0)
esito=Label(face, text="Esito: ")
esito.grid(row=1, column=3)

window.mainloop()
