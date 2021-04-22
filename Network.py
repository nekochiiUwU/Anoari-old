import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.26"
        self.port = 555
        self.addr = (self.server, self.port)
        self.Data = self.connect()

    def GetData1(self):
        Data = self.Data
        return Data

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            print("PASS")

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as error:
            print(error)
            return error

    def read_pos(self, DataIn):
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

    def make_Data(self, DataIn, Type):
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
