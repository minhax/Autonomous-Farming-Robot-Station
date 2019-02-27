from anytree import Node, RenderTree, LevelOrderIter
# Content: Robot Scheduler AI
# Purpose: Scheduler located on the Robot. Communicates w/ the Server. Receives Actions (Initiate, Work, Stop ..).
# Depending on the Action, gives the corresponding Task to execute in its tree structure
# Date : 12/07/2018

from src.Common import constant as const
from Commands.Tasks import *
import threading


class Scheduler:
    # Class must contain a reference to different objects he'll be interacting with : WeedingController, Navigation Manager
    # Class asking the command to carry out the request
    # Scheduler is in charge of connection to the serveur
    navigationController = None
    weedingController = None
    actions_tree = {"Initialize": RenderTree(const.action)}

    def __init__(self, navigation=None, weeding=None):
        # TODO : Remplacer par une liste chainee qui pop le premier element
        self._commands = []  # Internal use only
        self.navigationController = navigation
        self.weedingController = weeding
        self.mapping = None

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()

    def isworking(self, task):
        # In the future, we have to check some caracteristics about components. Then we can decide if they are fine or not
        status = Status("IsWorking")
        try:
            assert (status.message == "IsWorking")
            status.message = "Success"
        except AssertionError:
            status.message = "Error"

        # Add @status to @task
        task.status = status
        return task

class Worker(threading.Thread):

    def __init__(self, tree, scheduler):
        super(Worker, self).__init__()
        self.render_tree = tree
        self.scheduler = scheduler

    @staticmethod
    def create_task(self, task_name):

        # Example : lettuce_field
        method_name = task_name
        method = getattr(self, method_name, lambda: "Invalid task name, please check mispelling ")
        return method()

    # Iterate over tree, to find the interesting node
    # status : the name of the following node we are willing to find
    # tree : the render tree / sub-tree on which to search information
    @staticmethod
    def iterate_on_tree(self, status, tree):
        try:
            ''' We compare n.type to status.
             In a node, type can either be : Initiate, Success, Error
             Node names are tasks name
             '''
            nlist = [node.name for node in LevelOrderIter(tree, stop=lambda n: n.type is status)]
        # won't work, have to change this to assert if list is null
        except:
            exit("Empty")
        task = self.create_task(self, str(nlist[0]))
        task = self.scheduler.isworking(self.scheduler.navigationController, task)
        return task, nlist[0]

    def run(self):
        first_task = self.create_task(self, "sn") # give the first node
        first_task = self.scheduler.isworking(self.scheduler.navigationController, first_task)
        tree = self.render_tree
        while True:
            if message == "Empty":
                break
            # We return the task, on which we added a status
            task, tree = self.iterate_on_tree(self, message, tree)
            message = task.status.message