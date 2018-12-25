# Messages exchange test
from src.IA_Robot.src.Navigation.Controller import *
from src.IA_Robot.src.Scheduler.Scheduler import *
from src.Common.Commands.Actions import *

def start():
    # TODO : Fix server side for WebSocket
    # Client.initiate()
    # 1) Initialize Controllers and DP objects
    navigation = Controller()
    invoker = Invoker()
    # 2) Load XML File and create corresponding commands
    # 2) a) Initialization command for the Navigation Controller
    initialise_robot = initialization(navigation)
    # 3)
    invoker.store_command(initialise_robot)
    invoker.execute_commands()
    print("[Main] Navigation Controller Initialisation done")


if __name__ == '__main__':
    start()