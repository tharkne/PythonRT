import math

class vec3:
    """A 3D data structure used for holding point and other data"""

    x = 0.0
    y = 0.0
    z = 0.0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    # operator overload for vector addition
    def __add__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        assert not insinstance(scalar, vec3) # assure that vectors are not multiplied to each other
        return vec3(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __rmul__(self, scalar):
        # return vec3(self.x * scalar, self.y * scalar, self.z * scalar)
        return self.__mul__(scalar)

    def __str__(self):
        # return "<" + self.x + "," + self.y + "," + self.z + ">";
        return "({},{},{})".format(self.x, self.y, self.z)

    def dot(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)

    def mag(self):
        # return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        return math.sqrt(self.dot(self))

    def normalize(self):
        return self / mag(self)
    