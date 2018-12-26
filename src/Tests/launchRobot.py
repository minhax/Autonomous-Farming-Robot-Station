# Messages exchange test
from IA_Serveur.src.Mapping.Mapping import Mapping
from src.Robot.IA_Robot.src.Scheduler.Scheduler import *
from src.Robot.Navigation_Robot.src.Navigation.NavigationController import *
from src.Common.Commands.Actions import *
from Common.Parser.parser import Parser
from src.Robot.IA_Robot.src.Weeding.WeedingController import *


def start():
    print ("# ------ Robot Part1: Initialization ------ #")
    print("[Main] Loading XML File")
    # 1) Load XML File and create corresponding commands
    parser = Parser('../Common/Parser/files/robot.xml')
    robot = parser.object
    print("[Main] Creating Navigating and weeding Controllers")
    # 2) a) Initialization command for the Navigation NavigationController
    navigation_controller = NavigationController(robot)
    weeding_controller = WeedingController(robot)
    print("[Main] Creating Scheduler")
    # 2) b) Scheduler organizes and invoke commands for the NavigationController and the Weeding Controller
    invoker = Scheduler(navigation_controller, weeding_controller)
    # TODO: fix this when sockets are ready
    # So server knows there is a connected robot and can add it to his FleetManager
    print("[Main] Transferring information concerning robot to server ...")
    invoker.transfer_data_to_serveur(robot, "192.168.14.8", 1026)
    print(" ... Done")

    print("[Main] Initialise commands created")
    command_initialise_navigation = Initialization(navigation_controller)
    command_initialise_weeding = Initialization(weeding_controller)

    # 3) Store Commands
    invoker.store_command(command_initialise_navigation)
    invoker.store_command(command_initialise_weeding)
    print("[Main] All commands executed")
    # 4) Execute all commands in the dictionnary
    invoker.execute_commands()
    print (" # ------ Robot Part2 : Weeding ------- #")
    print("[Main] Receiving path planning from Server")
    # TODO: Put a waiting socket server waiting for connexion and for point_Dict
    # We fake this at the moment
    mapping = Mapping(robot)
    print("[Main] Initialise commands created")
    command_weeding_navigation = Weeding(navigation_controller, mapping)
    # command_weeding_weeding = Weeding(weeding_controller)

    invoker.store_command(command_weeding_navigation)
    # invoker.store_command(command_weeding_weeding)

    print("[Main] All commands executed")
    # 4) Execute all commands in the dictionnary
    invoker.execute_commands()


if __name__ == '__main__':
    start()