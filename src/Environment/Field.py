# Field xml contains two Elements containers : dimensions and floor
# The difference betweens fields remains in the elements inside those containers


class Field(object):

    dimDict = {}
    floorDict = {}
    attribute = None

    def __init__(self, attribute):
        self.type_of_attribute(self, attribute.getElementsByTagName('dimensions'))
        self.type_of_attribute(self, attribute.getElementsByTagName('floor'))

    @staticmethod
    def type_of_attribute(self, attribute):
        method_name = 'add_' + str(attribute[0].localName)
        self.attribute = attribute
        method = getattr(self, method_name, lambda: "Invalid type")
        return method(self)

    @staticmethod
    def add_dimensions(self):
        # We loop on all attributes
        for element in self.attribute[0].childNodes:
            if element.firstChild is None:
                pass
            else:
                self.dimDict[str(element.attributes['name'].value)] = str(element.firstChild.data)

            # TODO : Non-modular code
        print self.dimDict

    # status = Status("Error")

    @staticmethod
    def add_floor(self):

        for element in self.attribute[0].childNodes:
            if element.firstChild is None:
                pass
            else:
                self.floorDict[str(element.attributes['name'].value)] = str(element.firstChild.data)
            # TODO : Find a way to better handle problems
        print self.floorDict
#            status = Status("Error")
