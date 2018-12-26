import abc
import datetime

from Commands import Command


    # Actions are created when loading the XML file containing Actions for a particular entity.
    # An Action can trigger multiple tasks

class Action(Command):

    # Actions triggered by the operator
    # Receive a list of tasks when created, corresponding to tasks it has to execute in the Receiver

    def __init__(self, receiver):
        self._receiver = receiver
        self.tasks = []

    @abc.abstractmethod
    def execute(self):
        pass

# TODO Add method to dynamically create tasks depending on the action (or linked list?)

# Concrete Action class


class Initialization(Action):

    # Define a binding between a Receiver and an action. Implement Execute by invoking the
    # Corresponding operations(s) on Receiver
    def execute(self):
        self._receiver.initialize_simulation()


class Weeding(Action):

    # We store a mapping into the Command: Do the Weeding on this mapping
    def __init__(self, mapping):
        self.mapping = mapping
    # Define a binding between a Receiver and an action. Implement Execute by invoking the
    # Corresponding operations(s) on Receiver

    def execute(self):
        self._receiver.weeding_simulation(self.mapping)
