from Parser.parser import *
import json
from Websocket import Client
# Mapping manager


class Mapping(object):

    # Object can either be an Environment object, or a Machine object
    object = None
    parser = None
    websocket = None

    def __init__(self, xmlfile):
        parser = Parser()
        parser.start(xmlfile)
        self.parser = parser

    def sendMapToServer(self):

        jsonObject = json.dumps(self.parser.object)
        Client.ws.send(jsonObject)



