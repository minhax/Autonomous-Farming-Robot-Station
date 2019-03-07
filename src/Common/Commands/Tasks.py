from Commands import Command
from Status import Status
import abc
# Each Task has one status containing one message and a timestamp


class Tasks(Command):

    # Dictionnary containing timestamp as a key and Status msg as a Value

    def __init__(self, receiver):
        super(Tasks, self).__init__(receiver)
        self.status = Status()  # Tester si on voit bien default message

    @abc.abstractmethod
    def execute(self):
        pass

    def toString(self):
        print("Begin: {tsb} \n End:{tse} \n Delta:{tsd} \n Message:{msg} \n".format(tsb = self.status.beginTimeStamp, tse = self.status.endTimeStamp, tsd= self.status.computeTimes(),
                msg=self.status.message))
# Concrete Tasks class


class sync_navigator(Tasks):

    # Define a binding between a Receiver and an action. Implement Execute by invoking the
    # Corresponding operations(s) on Receiver
    def execute(self):
        status = self._receiver.sync_navigator_simulation()


class init_wheels(Tasks):

    # Define a binding between a Receiver and an action. Implement Execute by invoking the
    # Corresponding operations(s) on Receiver
    def execute(self):
        status = self._receiver.init_wheels_simulation()


class debug_sync_navigator(Tasks):

    # Define a binding between a Receiver and an action. Implement Execute by invoking the
    # Corresponding operations(s) on Receiver
    def execute(self):
        status = self._receiver.debug_sync_navigator_simulation()


class end_of_task(Tasks):

    # Define a binding between a Receiver and an action. Implement Execute by invoking the
    # Corresponding operations(s) on Receiver
    def execute(self):
        status = self._receiver.end_of_task_simulation()


class Task1_Weeding(Tasks):

    # We store a mapping into the Command: Do the Task1_Weeding on this mapping
    def __init__(self, receiver, mapping):
        super(Task1_Weeding, self).__init__(receiver)
        self.mapping = mapping
    # Define a binding between a Receiver and an action. Implement Execute by invoking the
    # Corresponding operations(s) on Receiver

    def execute(self):
        self._receiver.weeding_simulation(self.mapping)