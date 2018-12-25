# Parser test
from Mapping.Mapping import *
from Parser.parser import *


def start():

    parser = Parser('Parser/files/field.xml')
    Mapping(parser.object)
    parser = Parser('Parser/files/robot.xml')
    # Create mapping of object on


if __name__ == '__main__':
    start()