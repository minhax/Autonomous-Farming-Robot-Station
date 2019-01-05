# Messages exchange test
from IA_Robot.src.Scheduler.Scheduler import *
from Navigation_Robot.src.Navigation.NavigationController import *
from Commands.Actions import *

def start():
    # Client.initiate()
    # 1) Initialize Controllers and DP objects
    navigation = NavigationController()
    invoker = Scheduler(navigation)
    # 2) Load XML File and create corresponding commands
    # 2) a) sync_navigator command for the Navigation NavigationController done in the scheduller
    initialise_robot = sync_navigator(navigation)
    # 3)
    invoker.store_command(initialise_robot)
    invoker.execute_commands()
    print("[Main] Navigation NavigationController Initialisation done")


if __name__ == '__main__':
    start()