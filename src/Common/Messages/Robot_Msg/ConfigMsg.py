from Messages.Messages import *
from src.Serveur.IA_Serveur.src.Fleet.FleetManager import *


class ConfigMsg(Messages):
    # Configuration Messages, from Robot to Server.
    # Those messages transfer robot data

    def __init__(self, data):
        super(ConfigMsg, self).__init__(data)

    # On the server side, execution of treatment method

    def treatment(self, scheduler=None):
        fleet_manager = FleetManager.getInstance()
        fleet_manager.store_engine(self.data, "Created")
