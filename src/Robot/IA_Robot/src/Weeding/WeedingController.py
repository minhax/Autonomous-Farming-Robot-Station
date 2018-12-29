

class WeedingController:

    def __init__(self, receiver):
        # TODO Add builder for adding all the sensors
        self.roboticArm = None
        self.robot = receiver

    def initialize(self):

        # Check all navigation components status
        self.computeRoboticArmInfos()
        # Decorate with status
        # Add policy
        print ("Initialisation done for Weeding NavigationController")
        #
        pass

    @staticmethod
    def computeRoboticArmInfos():
        # TODO Create Status
        print("Robotic Arm is fine")

    def weeding(self):
        pass