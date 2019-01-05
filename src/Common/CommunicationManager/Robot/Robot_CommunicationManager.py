
from CommunicationManager.CommunicationManager import *


class Robot_CommunicationManager(CommunicationManager):

    socketservers = {}
    __instance = None

    def __init__(self, scheduler=None):
        super(Robot_CommunicationManager, self).__init__()
        self.localport = const.CLIENT_DEFAULT_PORT
        self.scheduler = scheduler
        if Robot_CommunicationManager.__instance is not None:
            raise Exception(" This class is a Singleton")
        else:
            Robot_CommunicationManager.__instance = self

    @staticmethod
    def getInstance(scheduler=None):
        if Robot_CommunicationManager.__instance is None:
            Robot_CommunicationManager(scheduler)
        return Robot_CommunicationManager.__instance

    # TODO : in the future, we might want to send data to other robots. We'll have to modify this
    @staticmethod
    def send_message_to_server(message):

        robotx1_client = Client(const.SERVER_DEFAULT_PORT, const.SERVER_IP_ADDRESS, message)
        robotx1_client.start()


