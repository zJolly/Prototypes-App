#!/usr/bin/python3

#-*- coding:UTF-8 -*-

import socket, time, subprocess

def parser(string):
	ita=""
	eng=""
	i=0
	fita=open('italiano.txt', 'r')
	feng=open('inglese.txt', 'r')
	ita, eng=string.split("#")
	print("Ita: "+ita)
	print("Eng: "+eng)
	fita0=fita.readlines()
	feng0=feng.readlines()
	if ita!="" and eng=="":
		string="Non trovata"
		for e in fita0:
			if e==ita+"\n":
				string=feng0[i].rstrip("\n")
			i+=1
	if eng!="" and ita=="":
		string="Non trovata"
		for e in feng0:
			if e==eng+"\n":
				string=fita0[i].rstrip("\n")
			i+=1
	if string=="#":
		string="Non trovata"
	fita.close()
	feng.close()
	return string

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
	string=c.recv(1024).decode()
	print("Messaggio dal client: "+string)
	reply=parser(string)
	c.send(reply.encode())
	print("Messaggio dal server: "+reply)
	c.close
	print("Connessione interrotta con  "+str(addr))
