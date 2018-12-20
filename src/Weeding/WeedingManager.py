

class WeedingManager:

    def __init__(self):
        # TODO Add code for Controller initialisation
        #TODO Add builder for adding all the sensors
        self.roboticArm = None


    def initialize(self):

        # Check all navigation components status
        self.computeRoboticArmInfos()
        # Decorate with status
        # Add policy
        print ("Initialisation done for Weeding Controller")
        #
        pass

    @staticmethod
    def computeRoboticArmInfos():
        #TODO Create Status
        print("Robotic Arm is fine")

    def startWeeding(self):
        pass