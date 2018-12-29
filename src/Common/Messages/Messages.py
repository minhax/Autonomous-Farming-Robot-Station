import abc


class Messages(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, data):
        self.data = data
        pass

    @abc.abstractmethod
    def treatment(self):
        pass

    # Methode Overriding
    def toString(self):
        pass
