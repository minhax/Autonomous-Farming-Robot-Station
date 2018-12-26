from Commands import Command
from Status import Status
import abc
# Each Task has one status containing one message and a timestamp


class Tasks(Command):

    # Dictionnary containing timestamp as a key and Status msg as a Value

    def __init__(self, receiver):
        self._receiver = receiver
        self.status = Status()  # Tester si on voit bien default message

    @abc.abstractmethod
    def execute(self):
        pass

    def toString(self):
        for status in self._status:
            print("Begin: {tsb} \n End:{tse} \n Delta:{tsd} \n Message:{msg} \n".format(tsb = status.beginTimeStamp, tse = status.endTimeStamp, tsd= status.computeTimes(),
                                      msg=status.message))
