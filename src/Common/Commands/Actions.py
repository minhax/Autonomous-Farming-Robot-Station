import abc
import datetime

from Commands import Command


    # Actions are created when loading the XML file containing Actions for a particular entity.
    # An Action can trigger multiple tasks

class Action(Command):

    # Actions triggered by the operator
    # Receive a list of tasks when created, corresponding to tasks it has to execute in the Receiver

    def __init__(self, receiver):
        super(Action, self).__init__(receiver)
        self._receiver = receiver
        self.tasks = []

    @abc.abstractmethod
    def execute(self):
        pass

# TODO Add method to dynamically create tasks depending on the action (or linked list?)


