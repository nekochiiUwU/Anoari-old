import socket
from _thread import *
import sys

print("Server Starting...")

server = "192.168.1.26"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as error:
    print(str(error))

s.listen(10)  # Limite d'utulisateurs sur le serveur

print("Connection...")

""" ==================== """


def Client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048) # Taille ded infos que je récupère
            reply = data.decode("utf-8")

            if not data:
                print("You are disconnected")
                break
            else:
                print("Recived informations", reply)
                print("Sending informations", reply)
            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost Connection")


""" ==================== """

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(Client, (conn,))  # Run en parallèle sur un autre thread
