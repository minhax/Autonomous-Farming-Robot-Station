import abc

# Content: Scheduler AI
# Additional content: Scheduler class for Command Design Pattern#
# Date : 12/07/2018


class Scheduler:

    # Class must contain a reference to different objects he'll be interacting with : WeedingController, Navigation Manager
    # Class asking the command to carry out the request
    # Scheduler is in charge of connection to the serveur

    navigationController = None
    weedingController = None

    def __init__(self, navigation=None, weeding=None):
        self._commands = []  # Internal use only
        self.navigationController = navigation
        self.weedingController = weeding

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()

