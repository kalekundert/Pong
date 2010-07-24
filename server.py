#!/usr/bin/python

import socket
import pickle

import Queue
import threading

from packets import *

class Host(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        # The client could be asking for information or trying to join the
        # game.  If they're looking for info, I can just send back a pre-
        # packaged string.  If they're trying to join, I need to:
        #
        # 1. Tell the client whether or not there is space left.
        # 2. Assign the client a unique ID.
        #    - This will be used to make sure that all the various managers
        #      running on different machines have unique IDs
        # 3. Get information about the player (maybe).

        while True:
            packet = Packet(client)
            request = packet.recieve()

            if request.type == "info":
                info = "Hosting a 1v1 game of Pong.\n"                  \
                       "There are 2 seats available."

                packet = Packet(client)
                packet.send("info", info)

            # This should end the thread
            elif request.type == "join":
                join = "Sorry, this feature has not been implemented yet"

                packet = Packet(client)
                packet.send("join", join)

            # This should also end the thread
            elif request.type == "quit":
                break

            else:
                print "Unrecognized request: '%s'." % request.type

        """'
        string = client.recv(4096)
        size, data = string.split("\0")
        packet = pickle.loads(data)

        if packet.type == "print":
            print packet.message
        if packet.type == "close":
            break
        '"""

server = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(("localhost", 15141))
    server.listen(5)

    print "Running the Pong server."

    clients = Queue.Queue(2)

    while not clients.full():
        client, address = server.accept()
        host = Host(client)
        host.start()

finally:
    server.close()
    print "Stopping the Pong server."
