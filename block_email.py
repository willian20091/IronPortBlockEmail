#!/usr/bin/env python3
#!/usr/bin/env bash

# -- Variaveis e importações ---

import subprocess
import os
import sys

#Hosts

HOST="192.168.0.100" 

# -- Métodos/def ---

def list_all_senders():
    sender_list = []
    senders = ""
    sender = ""
    sender_list = subprocess.getoutput('ssh ironport@' + HOST + ' "dictionaryconfig print LIST"')
    for i in sender_list.split("\n")[1:]:
        sender = i.split(",")[0].strip()
        senders.append(sender)
    return senders

def consulting_sender(url):
    if url in list_all_senders():
        return True
    else:
        return False

def remove_sender(url):
    return_consult = consulting_sender(url)
    if(return_consult):
        try:
            commit1 = subprocess.getoutput('ssh ironport@' + HOST + ' "dictionaryconfig edit LIST delete "' + url + '"; commit -y"')
            return True
        except:
            print("Erro no processo de desbloqueio")
    else:
        return False

def block_sender(url):
    return_consult = consulting_sender(url)
    if(return_consult):
        print("já está na lista")
        return False
    else:
        try:
            commit1 = subprocess.getoutput('ssh ironport@' + HOST + ' "dictionaryconfig edit LIST new "' + url + '"; commit -y"')
            return True
        except:
            print("Erro no processo de bloqueio")

def main():
    consulting("teste.com.br")

# -- Início ---

main()