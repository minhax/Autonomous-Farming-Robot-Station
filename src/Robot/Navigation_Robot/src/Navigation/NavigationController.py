from Common.Point import Point
from src.Common.Commands.Status import Status
import datetime
import time
import thread


class NavigationController:

    historian = []

    def __init__(self, receiver):
        # TODO Add builder for adding all the sensors
        # self.Lidar = None
        self.robot = receiver
        # Add HashMap

    def sync_navigator_simulation(self):

        # Check all navigation components status
        self.computeSensorInfos()

        print ("[Robot] Sync navigator done for NavigationController")
        return Status("Success")

    def init_wheels_simulation(self):

        # Check all navigation components status
        self.computeSensorInfos()

        print ("[Robot] Wheels for NavigationController")
        return Status("Success")

    def debug_sync_navigator_simulation(self):

        # Check all navigation components status
        self.computeSensorInfos()

        print ("[Robot] Debugging of sync Nav done for NavigationController")
        return Status("Success")

    def end_of_task_simulation(self):

        # Deactivate concerned component

        print ("[Robot] End of Task received, concerning component deactivated")
        return Status("Success")

    @staticmethod
    def computeSensorInfos():

        # 1) TODO Call sensors interfaces and return data
        # 2) TODO Process Data
        # 3) Change Status according to results
            # 3) a) Creation of the status request
        status = Status("Success")
        time.sleep(5)
        status.endTimeStamp = datetime.datetime.now().isoformat()

    @staticmethod
    def weeding_simulation(self, mapping):
        # TODO: Put a list of Actions TO DO before start working
        # Robot starts working, assume that initialization is done and functional to work
        # Workflow is the following :
        # Robot goes forward increasing its positions.
        # Every times there is a salad, he sends his coordinates

        thread.start_new(self.movement(), mapping)
        pass

    @staticmethod
    def movement(self, mapping):
        x = 0
        y = 0
        coord = Coordinates(x, y)
        i = 1
        while i < len(mapping.pointDict - 1):

            point = Point(mapping.pointDict["Point"+str(i)])
            if i % 2 == 0:
                while coord.y > point.y:
                    print ("[NavigationController] Robot in motion")
                    coord.y -= 10
                    thread.start_new(self.sendPosition(), self, coord)
            else:
                while coord.y < point.y:
                    print ("[NavigationController] Robot in motion")
                    coord.y += 10
                    thread.start_new(self.sendPosition(), self, coord)
            coord.x += 1

    @staticmethod
    def sendPosition( self, coord):
        # TODO : s communication for sending coordinates of the robot
        pass


class Coordinates:

    def __init__(self, x, y):
        self.x = x
        self.y = y
