from Common.CommunicationManager.Robot.Robot_CommunicationManager import *
from Messages.Messages import *


class MappingMsg(Messages):
    # Mapping Msg from Server to Robot

    def __init__(self, data):
        super(MappingMsg, self).__init__(data)

    # On the robot side, execution of treatment method
    def treatment(self, scheduler=None):
        super(MappingMsg, self).treatment()
        robot = Robot_CommunicationManager.getInstance()
        robot.scheduler.mapping = self.data