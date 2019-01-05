import abc


class Messages(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, data=None):
        self.data = data

    @abc.abstractmethod
    def treatment(self):
        pass

    # Methode Overriding
    def toString(self):
        pass
