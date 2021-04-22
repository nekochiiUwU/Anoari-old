import socket
from _thread import *
import sys

print("Server Starting...")

server = "192.168.1.26"
port = 555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as error:
    print("ERROR: ", str(error))

print(str(s))

s.listen(10)  # Limite d'utulisateurs sur le serveur

print("Connection...")

""" ==================== """


def read_pos(DataIn):
    Read = []
    for charactery in DataIn:
        Read.append(charactery)
    DataIn = Read
    Type = DataIn.pop(-1)
    if Type == "s":
        Data = "".join(DataIn)
    elif Type == "i":
        Data = int("".join(DataIn))
    elif Type == "f":
        Data = float("".join(DataIn))
    elif Type == "b":
        Data = bool("".join(DataIn))
    elif Type == "t":
        Data = "".join(DataIn)
        Data = list(Data.split(","))
        for item in range(len(Data)):
            Data[item] = int(Data[item])
        tuple(Data)
    elif Type == "l":
        Data = "".join(DataIn)
        Data = list(Data.split(","))
        for item in range(len(Data)):
            Data[item] = int(Data[item])
    else:
        Data = "".join(DataIn)
    return Data


def make_Data(DataIn, Type):
    if Type == "str":
        Data = DataIn + "s"

    elif Type == "int":
        Data = str(DataIn) + "i"

    elif Type == "float":
        Data = str(DataIn) + "f"

    elif Type == "bool":
        Data = str(DataIn) + "b"

    elif Type == "tuple":
        Data = ""
        for item in range(len(DataIn)):
            if item != 0:
                Data = Data + "," + str(DataIn[item])
            else:
                Data = str(DataIn[item])
        Data = Data + "t"

    elif Type == "list":
        Data = ""
        for item in range(len(DataIn)):
            if item != 0:
                Data = Data + "," + str(DataIn[item])
            else:
                Data = str(DataIn[item])
        Data = Data + "l"

    else:
        Data = DataIn + "?"
    return Data


def Client(conn, User):
    global Data
    conn.send(str.encode(make_Data(Data[1], "tuple")))
    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode("utf-8")  # data = données recus
            if data:
                Data[1] = read_pos(data)
                print("Recived informations from \tUser", User, ":\t", data)

            if not data:
                print("User", User, "is disconnected")
                break
            else:
                reply = make_Data(Data[1], "tuple")
                print("Sending informations to \tUser", User, ":\t", reply)
                conn.sendall(str.encode(reply))
        except error:
            print("error")
            break
    print("Lost Connection")


""" ==================== """

Data = [None, (40,0)]
UserId = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(Client, (conn, UserId))  # Run en parallèle sur un autre thread
    UserId += 1
