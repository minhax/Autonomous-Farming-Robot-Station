import abc
from src.Common import constant as const
from src.Common.Network.Serveur import *
from Common.Network.Client import *


class CommunicationManager(object):

    __metaclass__ = abc.ABCMeta
    number_socket_server = 0
    socketservers = {}
    localport = None
    __instance = None

    def __init__(self):
        pass

    def new_listening_socket_server(self):

        socket_server = Server(self.localport)
        socket_server.start()
        self.number_socket_server += 1
        # Verify if we can join thread when it's done, to retrieve the robot uuid?
        self.socketservers[socket_server.getName()] = ""

    def toString(self):
        print("Command from " + type(self._receiver).__name__)

    @staticmethod
    def send_message_to_localhost(message, port):

        client = Client("localhost", message, port)
        client.start()