class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    
    def __repr__(self):
        return 'Coordinate(' + str(self.x) + ', ' + str(self.y) + ')'
    

a = Coordinate(3, 4)

b = Coordinate(3, 4)

c = Coordinate(5, 6)

print(a == b)
print(a == c)

print(repr(a))
print(eval(repr(a)))
print(eval(repr(a)) == a)