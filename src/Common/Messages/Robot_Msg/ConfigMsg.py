from CommunicationManager.Server.Server_CommunicationManager import *
from Messages.Messages import *


class ConfigMsg(Messages):
    # Configuration Messages, from Robot to Server.
    # Those messages transfer robot data

    def __init__(self, robot_port, robot_ip_address, robot_id, data=None):
        super(ConfigMsg, self).__init__(data)
        self.local_client_port = robot_port
        self.client_ip_address = robot_ip_address
        self.robot_id = robot_id

    # On the server side, execution of treatment method
    def treatment(self, scheduler=None):

        communication_manager = Server_CommunicationManager.getInstance()
        # Using tuples so those values cannot be updated
        robot_info = (self.client_ip_address, self.local_client_port)
        # Store Robot UUID and Robot_Network information
        communication_manager.store_engine(self.data, robot_info)

