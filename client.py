#!/usr/bin/python

import socket
from packets import *

def prompt():
    return raw_input("> ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 15141))

packet = Packet(client)

try:
    print "Welcome to Pong!"
    command = prompt()

    while True:

        if command == "info":
            packet.send("info")
            print packet.recieve()

        elif command == "join":
            packet.send("join")
            print packet.recieve()

        elif command == "help":
            print "Coming soon."

        elif command == "quit":
            packet.send("quit")
            break

        else:
            print "Unrecognized command."

        command = prompt()

finally:
    client.close()
    print "Goodbye!"

"""'
while running:
    try:
        message = raw_input("> ")
        packet = Print(message)
    except EOFError:
        packet = Close()
        running = False

    string = str(packet)
    client.send(string)

client.close()
print
'"""
