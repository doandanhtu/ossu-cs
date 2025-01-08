class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        newSet = intSet()
        for val in self.vals:
            if other.member(val):
                newSet.insert(val)
        return newSet
    
    def __len__(self):
        return len(self.vals)
    

a = intSet()
b = intSet()
c = intSet()

a.insert(1)
a.insert(3)
a.insert(4)

b.insert(2)
b.insert(5)
b.insert(7)

c.insert(1)
c.insert(5)
c.insert(7)
c.insert(8)
c.insert(12)

print(a.intersect(b))
print(a.intersect(c))
print(b.intersect(c))

print(len(a))
print(len(c))
