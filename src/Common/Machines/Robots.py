from src.Common.Commands.Status import Status


class Robots(object):

    specsDict = {}
    equipmentDict = {}
    typeDict = {}
    inFleet = False
    _attribute = None
    status = Status("Inactive")

    def __init__(self, attribute):
        self.type_of_attribute(self, attribute.getElementsByTagName('type'))
        self.type_of_attribute(self, attribute.getElementsByTagName('specs'))
        self.type_of_attribute(self, attribute.getElementsByTagName('equipment'))
        self.IPAddress = None
        self.port = None

    @staticmethod
    def type_of_attribute(self, attribute):
        method_name = 'add_' + str(attribute[0].localName).lower()
        self._attribute = attribute
        method = getattr(self, method_name, lambda: "Invalid type")
        return method(self)

    @staticmethod
    def add_type(self):
        # Robot ought to be deployed in fleet
        # self.inFleet = _attribute.attributes['infleet'].value
        # TODO: Deploy fleet
        # 1) Insert this robot in the robot manager
        for element in self._attribute[0].childNodes:
            if element.firstChild is None:
                pass
            else:
                self.typeDict[str(element.attributes['name'].value)] = str(element.firstChild.data)
        print self.typeDict

    @staticmethod
    def add_specs(self):
        for element in self._attribute[0].childNodes:
            if element.firstChild is None:
                pass
            else:
                self.specsDict[str(element.attributes['name'].value)] = str(element.firstChild.data)
                # TODO : Find a way to better handle problems
        print self.specsDict

    @staticmethod
    def add_equipment(self):
        # We loop on all attributes
        for element in self._attribute[0].childNodes:
            if element.firstChild is None:
                pass
            else:
                self.equipmentDict[str(element.attributes['name'].value)] = str(element.firstChild.data)
                # TODO : Non-modular code
                self.status.message = "Inactive"
        print self.equipmentDict

    def get_robot_id(self):
        return self.typeDict["uuid"]