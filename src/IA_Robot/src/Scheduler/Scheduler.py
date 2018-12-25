import abc

# Content: Scheduler AI
# Additional content: Invoker class for Command Design Pattern#
# Date : 12/07/2018


class Invoker:

    # Class asking the command to carry out the request

    def __init__(self):
        self._commands = []  # Internal use only

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()

