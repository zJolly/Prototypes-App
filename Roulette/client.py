#!/usr/bin/python3

#-*- coding:UTF-8 -*-

import socket, os, time

def parser(string):
    s=socket.socket()
    host="127.0.0.1"
    port=12555
    s.connect((host, port))
    s.send(string.encode())
    reply=s.recv(1024).decode()
    if reply!="-ERR":
        esito, numero_estratto, puntata, vincita=reply.split("#")
        if esito=="+OK":
            print("Hai vinto "+vincita+"€ puntandone "+puntata)
        else:
            print("Hai perso")
    else:
        print("Errore")
    s.close()
    time.sleep(2)

while True:
    os.system("clear")
    print("0) Esci")
    print("1) Singolo")
    print("2) Split")
    print("3) Triple")
    scelta=input("Inserisci la scelta: ")
    time.sleep(1)
    os.system("clear")
    if scelta=="1":
        numero_fortunato_giocato=input("Inserisci il numero fortunato(0-36): ")
        puntata=input("Inserisci la puntata: ")
        singolo="SINGOLO#"+numero_fortunato_giocato+"#"+puntata
        parser(singolo)
    if scelta=="2":
        primo_numero_giocato=input("Inserisci il primo numero giocato(0-36): ")
        secondo_numero_giocato=input("Inserisci il secondo numero giocato(0-36): ")
        puntata=input("Inserisci la puntata: ")
        split="SPLIT#"+primo_numero_giocato+"#"+secondo_numero_giocato+"#"+puntata
        parser(split)
    if scelta=="3":
        primo_numero_giocato=input("Inserisci il primo numero giocato(0-36): ")
        secondo_numero_giocato=input("Inserisci il secondo numero giocato(0-36): ")
        terzo_numero_giocato=input("Inserisci il terso numero giocato(0-36): ")
        puntata=input("Inserisci la puntata: ")
        triple="Triple#"+primo_numero_giocato+"#"+secondo_numero_giocato+"#"+terzo_numero_giocato+"#"+puntata
        parser(triple)
    if scelta=="0":
        exit()
