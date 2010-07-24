import pickle

class Packet:
    def __init__(self, message, confirm=False):
        self.origin = messenger.address
        self.id = Packet.NEXT_ID
        Packet.ID += 1

        self.message = message
        self.reply = confirm

class Message:
    def __init__(self, type, ...):
        self.type = type
        self.data = ...

class Packet:
    def __init__(self, socket):
        self.socket = socket

    def __str__(self):
        return self.message

    def send(self, type, message=""):
        data = pickle.dumps({"type" : type, "message" : message})
        packet = "%d\0%s" % (len(data), data)
        self.socket.sendall(packet)

    def recieve(self):
        packet = self.socket.recv(4096)
        size, data = packet.split("\0")
        fields = pickle.loads(data)

        self.type = fields["type"]
        self.message = fields["message"]

        return self

class Close(Packet):
    def __init__(self):
        Packet.__init__(self, "close")

class Print(Packet):
    def __init__(self, message):
        Packet.__init__(self, "print")
        self.message = message
