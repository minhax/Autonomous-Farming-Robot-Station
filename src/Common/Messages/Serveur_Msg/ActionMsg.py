from Commands.Actions import Initialization
from IA_Robot.src.Scheduler.Scheduler import Scheduler
from Messages.Messages import *


class ActionMsg(Messages):

    # Actions triggered by the operator
    # Receive a list of tasks when created, corresponding to tasks it has to execute in the Receiver

    def __init__(self, data):
        super(ActionMsg, self).__init__(data)
        self.scheduler = None

    # On the other side, we execute the treatment method
    def treatment(self, scheduler=None):
        if scheduler is None:
            print "No Scheduler given, creating a new one"
            self.scheduler = Scheduler()
        self.scheduler = scheduler
        self.type_of_message(self)

    @staticmethod
    def type_of_message(self):
        # Example : Initialisation
        method_name = str(self.data).capitalize()
        method = getattr(self, method_name, lambda: "Invalid object, please check mispelling in XML file")
        return method(self)

    @staticmethod
    def Initialisation(self):
        command_initialise_navigation = Initialization(self.scheduler.navigationController)
        command_initialise_weeding = Initialization(self.scheduler.weedingController)

        self.scheduler.store_command(command_initialise_navigation)
        self.scheduler.store_command(command_initialise_weeding)

    @staticmethod
    def Weeding(self):
        pass

# TODO Add method to dynamically create tasks depending on the action (or linked list?)

# Concrete Action class
