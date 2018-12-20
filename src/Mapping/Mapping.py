from Parser.parser import *

# Will do websocket connexion to transfer information for mapping
# Mapping manager
class Mapping(object):

    def __init__(self, xmlfile):
        parser = Parser()
        parser.start(xmlfile)


