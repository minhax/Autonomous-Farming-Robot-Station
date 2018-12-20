import abc

class Command(object):

    # Add a receiver to the command
    __metaclass__ = abc.ABCMeta

    def __init__(self, receiver):
        self._receiver = receiver
        self._status_list = []


    @abc.abstractmethod
    def execute(self):
        pass

    #Methode Overriding
    def toString(self):
        print("Command from " + type(self._receiver).__name__)

