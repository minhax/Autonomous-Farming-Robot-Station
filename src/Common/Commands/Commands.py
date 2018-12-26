import abc


class Command(object):

    __metaclass__ = abc.ABCMeta

    # Add a receiver to the command
    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass

    # Methode Overriding
    def toString(self):
        print("Command from " + type(self._receiver).__name__)

