# coding: utf-8

import socket
import threading
from Common.Messages.Messages import *


class ClientThread(threading.Thread):

    def __init__(self, ip, port, client_socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.client_socket = client_socket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

    def run(self):
        print("Connexion de %s %s" % (self.ip, self.port,))

        msg, address = self.client_socket.recvfrom(2048)
        msg_cast = Messages(msg)
        msg_cast.treatment()

# TODO: Rajouter les informations du sendeur
        print("Client déconnecté...")


class Server(threading.Thread):

    def __init__(self, port=1111):
        super(Server, self).__init__()
        self.tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcpsock.bind(("", port))

    def run(self):
        while True:
            self.tcpsock.listen(10)
            print("Server currently listening...")
            (clientsocket, (ip, port)) = self.tcpsock.accept()
            newthread = ClientThread(ip, port, clientsocket)
            newthread.start()