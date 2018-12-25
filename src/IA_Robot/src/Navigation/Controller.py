
from src.Common.Commands.Status import Status
import datetime
import time


class Controller:

    def __init__(self):
        # TODO Add code for Controller initialisation
        # TODO Add builder for adding all the sensors
        self.Lidar = None


    def initialize(self):

        # Check all navigation components status
        self.computeSensorInfos()
        # Add policy
        print ("Initialisation done for Navigation Controller")

    @staticmethod
    def computeSensorInfos():

        # 1) TODO Call sensors interfaces and return data
        # 2) TODO Process Data
        # 3) Change Status according to results
            # 3) a) Creation of the status request
        status = Status("COMPLETE")
        time.sleep(5)
        status.endTimeStamp = datetime.datetime.now().isoformat()

    @staticmethod
    def startWeeding(self):
        pass

