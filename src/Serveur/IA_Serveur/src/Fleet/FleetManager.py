
# Content: FleetManager
# Additional content: Scheduler class for Command Design Pattern#
# Date : 12/07/2018
# Purpose: Manager on Server side, controlling how many robots/drone are currently active


class FleetManager:

    # Class asking the command to carry out the request
    machines = {}
    __instance = None

    @staticmethod
    def getInstance():
        if FleetManager.__instance is None:
            FleetManager()
        return FleetManager.__instance

    def __init__(self):
        if FleetManager.__instance is not None:
            raise Exception(" This class is a Singleton")
        else:
            FleetManager.__instance = self

    def store_engine(self, machine, status):
        self.machines[machine] = status

    def remove_engine(self, engine):
        self.machines.pop(engine, None)


