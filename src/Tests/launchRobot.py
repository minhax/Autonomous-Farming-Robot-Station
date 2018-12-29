# Messages exchange test
from IA_Serveur.src.Mapping.Mapping import Mapping
from Messages.Robot_Msg.ConfigMsg import ConfigMsg
from src.Robot.IA_Robot.src.Scheduler.Scheduler import *
from src.Robot.Navigation_Robot.src.Navigation.NavigationController import *
from src.Common.Commands.Actions import *
from Common.Parser.parser import Parser
from src.Robot.IA_Robot.src.Weeding.WeedingController import *
from src.Common.Network.Serveur import *
from src.Common import constant as const
from src.Common.Network.Client import Client


def start():
    print ("# ------ Robot Part1: Initialization ------ #")
    print("[Main] Loading XML File")
    # 1) Load XML File and create corresponding commands
    parser = Parser('../Common/Parser/files/robot.xml')
    robot = parser.obj
    print("[Main] Creating Navigating and weeding Controllers")
    # 2) a) Initialization command for the Navigation NavigationController
    navigation_controller = NavigationController(robot)
    weeding_controller = WeedingController(robot)
    print("[Main] Creating Scheduler")
    # 2) b) Scheduler organizes and invoke commands for the NavigationController and the Weeding Controller
    scheduler = Scheduler(navigation_controller, weeding_controller)

    # 3) Transfer connexion information to server
    print("[Main] Transferring information concerning robot to server ...")
    msg = ConfigMsg(robot)
    msg.treatment()
    client = Client(const.SERVER_IP_ADDRESS, msg, const.SERVER_DEFAULT_PORT)
    client.start()
    # Attention, on lance un nouveau thread, donc y'a pas d'attente
    print(" ... Done")

    print("[Main] Launch Socket server")
    socket_server = Server(1111)
    # Server socket receives message from server
    # It applies message.treatment(), doing the correct behaviour
    socket_server.start()
    # Attention, multithread, donc rien ne sera execute

    # 4) Execute all commands in the dictionnary
    scheduler.execute_commands()
    print("[Main] All commands executed")
    print (" # ------ Robot Part2 : Weeding ------- #")
    # We fake this at the moment
    mapping = Mapping(robot)
    print("[Main] Initialise commands created")
    command_weeding_navigation = Weeding(navigation_controller, mapping)
    # command_weeding_weeding = Weeding(weeding_controller)

    scheduler.store_command(command_weeding_navigation)
    # scheduler.store_command(command_weeding_weeding)

    print("[Main] All commands executed")
    # 4) Execute all commands in the dictionnary
    scheduler.execute_commands()


if __name__ == '__main__':
    start()