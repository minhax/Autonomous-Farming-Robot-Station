# Parser test
from Mapping.Mapping import Mapping
from Parser.parser import Parser


def start():

    parser = Parser('Parser/files/field.xml')
    Mapping(parser.object)
    parser = Parser('Parser/files/robot.xml')
    # Create mapping of object on


if __name__ == '__main__':
    start()