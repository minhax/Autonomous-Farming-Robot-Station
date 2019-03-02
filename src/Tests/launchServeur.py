# Messages exchange test

from Parser.parser import Parser
from src.Serveur.IA_Serveur.src.Mapping.Mapping import Mapping
from Messages.Serveur_Msg.MappingMsg import *
from CommunicationManager.Server.Server_CommunicationManager import *
# Start thread is initializing Server components, and then create WebSocket Server and Socket servers.
# it's then
def start():

    print ("# ------ Server Part1: Server sync_navigator ------ #")
    # 1) First actions : Parser and Mapping for the field
    print("[Main] Loading XML File")

    parser = Parser('../Common/Parser/files/field.xml')

    mapping = Mapping(parser.obj)
    headers = {'content-type': 'field initialisation'}

    # ------ Web server not working atm ------- #
    # Server_CommunicationManager.send_data_to_webserver(mapping, headers)

    # 2) Initiate components : Robot_CommunicationManager, websocket
    # 3)Launch WebSocket and send the field Mapping
    # Through WebSocket, User can decide to add more machines or not. If so, we increment local port, and open a new socket_server
    com_manager = Server_CommunicationManager.getInstance()


    print ("# ------ End of initialisation ------ #")
    print ("# ------ Server Part2: sync_navigator information exchange  ------ #")
    # Create new thread for s server listening
    # 6) Connect with robot
    com_manager.new_listening_socket_server()
    print ("# ------ Robot connection and setup done ------ #")
    # 8) Send mapping to Robot
    message = MappingMsg(mapping.pointDict)
    # Let's imagine we want to communicate with robot "x248482"
    # This information will be provided by the websocket
    robot1 = "x248482"
    # com_manager.send_message_to_robot(message, com_manager.get_robot_info(robot1))
    CommunicationManager.send_message_to_localhost(message, const.CLIENT_DEFAULT_PORT)
    '''
    print ("# ------ Server Part3: Sending orders to robot ------ #")
    # 8) When receiving orders from webSocket, send Actions to Robots.
    msg = ActionMsg("initialize")
    #com_manager.send_message_to_robot(msg, com_manager.get_robot_info(robot1))
    CommunicationManager.send_message_to_localhost(msg, const.CLIENT_DEFAULT_PORT)
    # TODO: maybe multicast it?
    print("[Main] Navigation NavigationController Initialisation done")

    # TODO: Websocket
    # 6) Send robot information to web server
    '''


if __name__ == '__main__':
    start()