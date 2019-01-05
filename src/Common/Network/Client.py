# coding: utf-8
import json
import socket
import threading
import pickle


class Client(threading.Thread):

    destination_address = None
    destination_port = None
    s = None

    def __init__(self, address_ip, message, port=1111):
        super(Client, self).__init__()
        self.destination_address = address_ip
        self.message = message
        self.destination_port = port

    def run(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.destination_address, self.destination_port))
        print("Sending Message:")
        # Do we need serialization in Python?
        self.s.sendall(pickle.dumps(self.message))
        #self.s.sendall(json.dumps(self.message))
        # Is close necessary?
        self.s.close()
        print("Message sent:")