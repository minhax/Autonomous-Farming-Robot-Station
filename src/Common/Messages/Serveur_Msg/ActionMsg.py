from Commands.Tasks import sync_navigator, Task1_Weeding
from IA_Robot.src.Scheduler.Scheduler import Scheduler, Worker
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
        else:
            self.scheduler = scheduler
        self.type_of_message(self)

    @staticmethod
    def type_of_message(self):
        # Example : Initialisation
        method_name = str(self.data).capitalize()
        method = getattr(self, method_name, lambda: "Invalid object, please check mispelling in XML file")
        return method(self)

    @staticmethod
    def Initialize(self):

        # Chercher l'arbre initialisation
        tree = self.scheduler.actions_tree["Initialize"].getValue()

        # Retourner le nombre de premier fils de premier etage qu'on a , et lancer un worker par fils
        init_worker = Worker(tree, self.scheduler)
        init_worker.start()

        command_initialise_weeding = sync_navigator(self.scheduler.weedingController)
        self.scheduler.store_command(command_initialise_weeding)
        # faire executer la tache pour le receiver

        self.scheduler.execute_commands()

        # Once operations are executed, we retrieve the previous command, which will have been decorated with a Status
        # We then, in the thread, analyse the status we have, and we decide which operation to do


    @staticmethod
    def Weeding(self):
        command_weeding_navigation = Task1_Weeding(self.scheduler.navigationController, self.scheduler.mapping)

        # command_weeding_weeding = Task1_Weeding(weeding_controller)

        self.scheduler.store_command(command_weeding_navigation)
        # scheduler.store_command(command_weeding_weeding)

        print("[Main] All commands executed")
        # 4) Execute all commands in the dictionnary
        self.scheduler.execute_commands()


# Concrete Action class
