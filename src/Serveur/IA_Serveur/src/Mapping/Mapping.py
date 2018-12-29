import json
from src.Serveur.IA_Serveur.src.Websocket.Client import *
from Common.Point import Point
# Mapping manager


class Mapping(object):

    # Global websocket variable
    # websocket = None
    x = 0
    y = 0

    def __init__(self, obj):

        # Object can either be an Environment object, or a Machine object
        self.obj = obj
        self.pointDict = {}
        self.generateDict(self)
        # self.sendMapToServer(self.pointDict)

    @staticmethod
    def sendMapToServer(self, item):

        jsonObject = json.dumps(item)
        #ws.send(jsonObject)

    @staticmethod
    def generateDict(self):

        # Depending on rows in self.object.dimDict, calculate number of points
        pointsnumber = int(self.obj.dimDict.get("rows")) * 2

    # for loop from point 0 to point pointsnumber. We decide that point 0 is at the beginning of the first row
        point0 = Point(0, 0)

        point0.name = "Point" + str(0)
        self.pointDict[point0.name] = point0

        point1 = Point(0, int(self.obj.dimDict.get("length")))
        point1.name = "Point" + str(1)
        self.pointDict[point1.name] = point1

        for x in range(2, pointsnumber):
            point = Point(Mapping.x, Mapping.y)
            point.name = "Point" + str(x)
            if x % 2 == 0:
                Mapping.y = 0
                Mapping.x += int(self.obj.dimDict.get("distanceBetweenRows"))

            else:
                Mapping.y = int(self.obj.dimDict.get("length"))
                Mapping.x += int(self.obj.dimDict.get("distanceBetweenRows"))

            self.pointDict[point.name] = point

        print self.pointDict
        print self.pointDict.__len__()



    # Create and associate those points as a double linked list with coordinate as sdata  (calculate)
    # Create a Json
    # {
    #    "PointDict": [{
    #        "name": "Point A",
    #        "x": 4000,
    #        "y": 5000
    #    },
    #        {
    #            "name": "Point B",
    #            "x": 4500,
    #            "y": 5000
    #        }
    #    ]
    # }
    # Using double linked list allows to make robot know where they are going, and there next target once they've reached it.
    # Moreover, as there might be several robots on the same field, it helps coordinate their actions by knowing where each robot is.




class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
