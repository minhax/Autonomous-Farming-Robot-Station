class Point(object):

    nbPoints = 0

    def __init__(self, x = 0 , y = 0):
        self.x = x
        self.y = y
        self.id = Point.nbPoints
        self.name = None
        Point.nbPoints += 1

    def printNumberPoints(self):
        print "Currently " + Point.nbPoints + "points on the field"