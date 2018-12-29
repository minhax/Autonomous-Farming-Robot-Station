# coding: utf-8

import socket
import threading


class Client(threading.Thread):

    destination_address = None
    destination_port = None
    socket = None

    def __init__(self, address_ip, message, port=1111):
        super(Client, self).__init__()
        self.destination_address = address_ip
        self.message = message
        self.destination_port = port

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.destination_address, self.destination_port))
        file_name = None
        print("Sending Message:")
        socket.send(file_name.encode())