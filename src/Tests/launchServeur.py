# Messages exchange test
from Commands.Actions import *
from src.Serveur.IA_Serveur.src.Fleet.FleetManager import FleetManager
from Parser.parser import Parser
from src.Serveur.IA_Serveur.src.Mapping.Mapping import Mapping
def start():
    print ("# ------ Server Part1: Initialization ------ #")
    print("[Main] Loading XML File")
    parser = Parser('Parser/files/field.xml')
    Mapping(parser.object)

    # 2) Initiate components
    fleetManager = FleetManager.getInstance()
    # Websocket
    # ServerSocket
    # 3)Launch WebSocket and send the field Mapping
    print ("# ------ End of initialisation ------ #")
    print ("# ------ Server Part2: Waiting for robot connection  ------ #")
    # 4) Wait for robot connection!
    # 5) Once robot is connected, retrieve its information, store them into fleetManager
    # 6) Send robot information to web server
    # 7) Connect with robot and send path planning
    print ("# ------ Robot connection and setup done ------ #")
    print ("# ------ Server Part3: Sending orders to robot ------ #")
    # 8) When receiving orders from webSocket, send Actions to Robots.
    # TODO: maybe multicast it?
    # TODO : Fix server side for WebSocket
    print("[Main] Navigation NavigationController Initialisation done")


if __name__ == '__main__':
    start()