from xml.dom import minidom
from Environment.Field import Field
from Fleet.FleetManager import *

# parse an xml file by name
# determine which type of xml we are loading
# Using parser object, we can determine a specific behaviour for every type
from Machines.Robots import Robots


class Parser(object):

    dom = None
    type = None

    def start(self, argument):
        # self.dom = main DOM object
        self.dom = minidom.parse(argument)
        # self.type = type DOM
        self.type = self.dom.getElementsByTagName('type')
        self.type_of_object(self)

    @staticmethod
    def type_of_object(self):

        # Example : lettuce_field
        method_name = str(self.type[2].firstChild.data) + '_' + str(self.type[1].firstChild.data)
        method = getattr(self, method_name, lambda: "Invalid object, please check mispelling in XML file")
        return method(self)

    # In case we have a lettuce field, we retrieve information and create corresponding objects
    @staticmethod
    def lettuce_field(self):
        # Create the field and set its attribute
        field = Field(self.dom)
        return field
        # TODO Temporarely : Print result
        #map(lambda x : print x, field.floordict)
        # TODO Long Time : Send information through websocket to your server where you will do a mapping

    @staticmethod
    def strawberry_field(self):
        #TODO
        field = Field(self.dom)
        return field

    @staticmethod
    def R1_robot(self):
        # TODO
        robot = Robots(self.dom)
        fleetmanager = FleetManager.getInstance()
        fleetmanager.store_engine(robot, "Created")

# Use unlink() function to free memory at the end


