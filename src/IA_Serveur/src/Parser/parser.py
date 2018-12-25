from xml.dom import minidom
from src.IA_Serveur.src.Environment.Field import Field

# parse an xml file by name
# determine which type of xml we are loading
# Using parser object, we can determine a specific behaviour for every type
from src.IA_Serveur.src.Machines.Robots import Robots
from src.IA_Serveur.src.Fleet.FleetManager import FleetManager


class Parser(object):

    def __init__(self, argument):

        self.object = None
        # main DOM object
        self.dom = minidom.parse(argument)
        # self.type = type DOM
        self.type = self.dom.getElementsByTagName('type')

        self.type_of_object(self)

    @staticmethod
    def type_of_object(self):

        # Example : lettuce_field
        method_name = str(self.type[2].firstChild.data).lower() + '_' + str(self.type[1].firstChild.data).lower()
        method = getattr(self, method_name, lambda: "Invalid object, please check mispelling in XML file")
        return method(self)

    # In case we have a lettuce field, we retrieve information and create corresponding objects
    @staticmethod
    def lettuce_field(self):
        # Create the field and set its attribute
        self.object = Field(self.dom)
        # TODO Temporarely : Print result
        #map(lambda x : print x, field.floordict)
        # TODO Long Time : Send information through websocket to your server where you will do a mapping

    @staticmethod
    def strawberry_field(self):
        #TODO
        self.object = Field(self.dom)

    @staticmethod
    def r1_robot(self):
        # TODO
        self.object = Robots(self.dom)
        fleetmanager = FleetManager.getInstance()
        fleetmanager.store_engine(self.object, "Created")





# Use unlink() function to free memory at the end


