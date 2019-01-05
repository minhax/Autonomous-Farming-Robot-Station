
from src.Common import constant as const
from src.Common.Network.Serveur import *
from Common.Network.Client import *
from CommunicationManager.CommunicationManager import *


class Server_CommunicationManager(CommunicationManager):

    machines = {}
    websocket = None
    socketservers = {}
    __instance = None

    def __init__(self):
        super(Server_CommunicationManager, self).__init__()
        self.localport = const.SERVER_DEFAULT_PORT
        if Server_CommunicationManager.__instance is not None:
            raise Exception(" This class is a Singleton")
        else:
            Server_CommunicationManager.__instance = self

    @staticmethod
    def getInstance():
        if Server_CommunicationManager.__instance is None:
            Server_CommunicationManager()
        return Server_CommunicationManager.__instance

    def store_engine(self, machine, robot_info):
        self.machines[machine] = robot_info

    def get_robot_info(self, key):
        return self.machines[key]

    def remove_engine(self, engine):
        self.machines.pop(engine, None)

    # TODO : in the future, we might want to send data to other robots. We'll have to modify this
    def send_message_to_robot(self, message, robot_uuid):

        robot_info = self.get_robot_info(robot_uuid)
        # Square brackets to slice data. [0] is the robot IP adress, [1] is the local port he should be contacted on
        robotx1_client = Client(robot_info[0], robot_info[1], message)
        robotx1_client.start()


