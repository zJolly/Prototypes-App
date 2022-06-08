#!/usr/bin/python3

#-*- coding:UTF-8 -*-

import socket, time, subprocess, random

def parser(stringclient):
    numero_estratto=random.randint(0, 36)
    print("Numero estratto"+str(numero_estratto))
    first_word=stringclient.split("#")[0]
    print(first_word)

    if first_word=="SINGOLO":
        first_word, numero_fortunato_giocato, puntata=stringclient.split("#")
        numero_fortunato_giocato=int(numero_fortunato_giocato)
        puntata=int(puntata)
        if numero_fortunato_giocato<=36 and numero_fortunato_giocato>=0:
            if numero_fortunato_giocato==numero_estratto:
                vincita=puntata*35
                stringclient="+OK#"+str(numero_estratto)+"#"+str(puntata)+"#"+str(vincita)
            else:
                vincita=0
                stringclient="+KO#"+str(numero_estratto)+"#"+str(puntata)+"#"+str(vincita)
        else:
            stringclient="-ERR"
        print("Singolo")
    if first_word=="SPLIT":
        first_word, primo_numero_giocato, secondo_numero_giocato, puntata=stringclient.split("#")
        primo_numero_giocato=int(primo_numero_giocato)
        secondo_numero_giocato=int(secondo_numero_giocato)
        puntata=int(puntata)
        if primo_numero_giocato<=36 and primo_numero_giocato>=0 and secondo_numero_giocato<=36 and secondo_numero_giocato>=0:
            if primo_numero_giocato==numero_estratto or secondo_numero_giocato==numero_estratto:
                vincita=puntata*17
                stringclient="+OK#"+str(numero_estratto)+"#"+str(puntata)+"#"+str(vincita)
            else:
                vincita=0
                stringclient="+KO#"+str(numero_estratto)+"#"+str(puntata)+"#"+str(vincita)
        else:
            stringclient="-ERR"
        print("Split")
    if first_word=="Triple":
        first_word, primo_numero_giocato, secondo_numero_giocato, terzo_numero_giocato, puntata=stringclient.split("#")
        primo_numero_giocato=int(primo_numero_giocato)
        secondo_numero_giocato=int(secondo_numero_giocato)
        terzo_numero_giocato=int(terzo_numero_giocato)
        puntata=int(puntata)
        if primo_numero_giocato<=36 and primo_numero_giocato>=0 and secondo_numero_giocato<=36 and secondo_numero_giocato>=0 and terzo_numero_giocato<=36 and terzo_numero_giocato>=0:
            if primo_numero_giocato==numero_estratto or secondo_numero_giocato==numero_estratto or terzo_numero_giocato==numero_estratto:
                vincita=puntata*11
                stringclient="+OK#"+str(numero_estratto)+"#"+str(puntata)+"#"+str(vincita)
            else:
                vincita=0
                stringclient="+KO#"+str(numero_estratto)+"#"+str(puntata)+"#"+str(vincita)
        else:
            stringclient="-ERR"
        print("Triple")

    return stringclient

host="127.0.0.1"
port=12555
subprocess.Popen("fuser -k "+str(port)+"/tcp", shell=True)
print("Porta di servizio libera")
time.sleep(3)
print("Server avviato")

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

while(True):
	c, addr=s.accept()
	print("Connessione stabilita con "+str(addr))
	inputmessage=c.recv(1024).decode()
	print("Messaggio dal client: "+inputmessage)
	outputmessage=parser(inputmessage)
	c.send(outputmessage.encode())
	print("Messaggio dal server: "+outputmessage)
	c.close
	print("Connessione interrotta con  "+str(addr))
