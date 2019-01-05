# Messages exchange test
from Messages.Robot_Msg.ConfigMsg import ConfigMsg
from src.Robot.IA_Robot.src.Scheduler.Scheduler import *
from src.Robot.Navigation_Robot.src.Navigation.NavigationController import *
from Common.Parser.parser import Parser
from src.Robot.IA_Robot.src.Weeding.WeedingController import *
from CommunicationManager.Robot.Robot_CommunicationManager import *


def start():
    print ("# ------ Robot Part1: sync_navigator ------ #")
    print("[Main] Loading XML File")
    # 1) Load XML File and create corresponding commands
    parser = Parser('../Common/Parser/files/robot.xml')
    robot = parser.obj
    print("[Main] Creating Navigating and weeding Controllers")
    # 2) a) sync_navigator command for the Navigation NavigationController
    navigation_controller = NavigationController(robot)
    weeding_controller = WeedingController(robot)
    print("[Main] Creating Scheduler")
    # 2) b) Scheduler organizes and invoke commands for the NavigationController and the Task1_Weeding Controller
    scheduler = Scheduler(navigation_controller, weeding_controller)
    print(" [Main] Launch RobotCommunicationManager")
    com_manager = Robot_CommunicationManager.getInstance(scheduler)

    print("[Main] Launch Socket server")
    # Launch a server s, always listening
    com_manager.new_listening_socket_server()

    '''# 3) Transfer connexion information to server
    print("[Main] Transferring information concerning robot to server ...")
    msg = ConfigMsg(const.CLIENT_DEFAULT_PORT, "192.168.14.2", robot.get_robot_id, robot)  # Local port on which server can communicate

    # Robot_CommunicationManager.send_message_to_server(msg)
    CommunicationManager.send_message_to_localhost(msg, const.CLIENT_DEFAULT_PORT)
    print(" ... Done")
    print (" # ------ Robot Part2 : Task1_Weeding ------- #")
    print("[Main] Initialise commands created")

    # Task1_Weeding action for the navigation controller includes autonomous vehicle guidance on mapping
    # command_weeding_navigation = Task1_Weeding(navigation_controller, mapping)
    # command_weeding_weeding = Task1_Weeding(weeding_controller)

    # scheduler.store_command(command_weeding_navigation)
    # scheduler.store_command(command_weeding_weeding)

    print("[Main] All commands executed")
    # 4) Execute all commands in the dictionnary
    #scheduler.execute_commands()
    '''

if __name__ == '__main__':
    start()