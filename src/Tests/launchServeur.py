# Messages exchange test
from src.Serveur.IA_Serveur.src.Fleet.FleetManager import FleetManager
from Parser.parser import Parser
from src.Serveur.IA_Serveur.src.Mapping.Mapping import Mapping
from Common.Network.Serveur import *
from Messages.Serveur_Msg.ActionMsg import *
from Common.Network.Client import *
from src.Common import constant as const

# Start thread is initializing Server components, and then create WebSocket Server and Socket servers.
# it's then
def start():

    print ("# ------ Server Part1: Server Initialization ------ #")
    print("[Main] Loading XML File")
    parser = Parser('../Common/Parser/files/field.xml')
    Mapping(parser.obj)

    # 2) Initiate components
    # TODO: Websocket
    # Through WebSocket, User can decide to add more machines or not. If so, we increment local port, and open a new socket_server
    # This code will be moved in the web socket, triggered by the human
    localport = const.SERVER_DEFAULT_PORT
    socket_server = Server(localport)
    socket_server.start()

    # 3)Launch WebSocket and send the field Mapping

    print ("# ------ End of initialisation ------ #")
    print ("# ------ Server Part2: Waiting for robot connection  ------ #")
    # TODO : Comment detecter qu'un robot s'est connecte??
    # 6) Send robot information to web server
    # 7) Connect with robot and send path planning
    fleet_manager = FleetManager.getInstance()
    #robotx1_client = Client(robot_IPAddress, robot_port, msg)
    #robotx1_client.start()
    print ("# ------ Robot connection and setup done ------ #")
    print ("# ------ Server Part3: Sending orders to robot ------ #")

    # 8) When receiving orders from webSocket, send Actions to Robots.
    msg = ActionMsg("initialize")
    robot1Client = Client(robot_IPAddress, robot_port, msg)
    robot1Client.start()
    # TODO: maybe multicast it?
    # TODO : Fix server side for WebSocket
    print("[Main] Navigation NavigationController Initialisation done")


if __name__ == '__main__':
    start()