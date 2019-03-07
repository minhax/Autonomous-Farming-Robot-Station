
# Content: RobotManager
# Additional content: Scheduler class for Command Design Pattern#
# Date : 12/07/2018
# Purpose: Manager on Server side, controlling how many robots/drone are currently active


class RobotManager:

    # Class asking the command to carry out the request
    machines = {}
    __instance = None

    @staticmethod
    def getInstance():
        if RobotManager.__instance is None:
            RobotManager()
        return RobotManager.__instance

    def __init__(self):
        if RobotManager.__instance is not None:
            raise Exception(" This class is a Singleton")
        else:
            RobotManager.__instance = self

    def store_engine(self, machine, IPAddress, port):
        info = IPAddress + '::' + str(port)
        self.machines[machine] = info

    def remove_engine(self, engine):
        self.machines.pop(engine, None)


