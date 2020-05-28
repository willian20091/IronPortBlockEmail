#!/usr/bin/env python3
#!/usr/bin/env bash

# -- Imports ---

import subprocess
import os
import sys

#Hosts

HOST="192.168.0.100" 

# -- def ---

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
            print("Unlocking process error")
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
            print("Blocking process error")

def main():
    print(list_all_senders())
    consulting("teste.com.br")
    block_sender(teste.com.br)
    remove_sender("teste.com.br")

# -- main ---

main()