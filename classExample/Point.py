# Point.py
# Defines a class to represent two dimensional discrete points.

class Point:
    def __init__(self,x=0,y=0):
        self.xCord = x
        self.yCord = y

    def __str__(self):
        return "(" + str(self.xCord) + "," + str(self.yCord) + ")"

    def getX(self):
        return self.xCord

    def getY(self):
        return self.yCord

    def shift(self, xInc, yInc):
        self.xCord = self.xCord + xInc
        self.yCord = self.yCord + yInc
print "--"*10, "before shift B", "--"*10
pointA = Point(5,5)
pointB = Point()
print pointA
print pointB

pointB.shift(3,3)
print "--"*10, "after shift B", "--"*10
print pointA
print pointB
