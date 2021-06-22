from decimal import *
import math

getcontext().prec = 10

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __sub__(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __mul__(self, v):
        if isinstance(v, int) or isinstance(v, float) or isinstance(v, Decimal):
            new_coordinates = [x*Decimal(v) for x in self.coordinates]
            return Vector(new_coordinates)
        elif isinstance(v, Vector):
            return self.dot(v)

    def len(self):
        return sum([x**2 for x in self.coordinates]).sqrt()

    def norm(self):
        len = self.len()
        if len == Decimal(0):
            return self
        return self*(Decimal(1.0)/len)

    def dot(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    def angle(self, v, in_degrees=False):
        """
        angle between vectors
        by default in radians
        """
        cos = self.norm() * v.norm()
        rad = math.acos(cos)
        if in_degrees:
            return math.degrees(rad)
        return rad

    def proj_parallel(self, v):
        """
        parallel projection to v
        """
        v_norm = v.norm()
        return v_norm * (self * v_norm)

    def proj_orthogonal(self, v):
        """
        orthogonal projection to v
        """
        return (self-self.proj_parallel(v))

    def cross_product(self, v):
        (x1, y1, z1) = self.coordinates
        (x2, y2, z2) = v.coordinates
        x3 = y1*z2 - y2*z1
        y3 = -(x1*z2 - x2*z1)
        z3 = x1*y2 - x2*y1
        return Vector([x3,y3,z3])

    def area_parallelogram(self, v):
        return (self.cross_product(v).len())


v1 = Vector([1,2,3])
v2 = Vector([5,6,7])

print("sum: {}".format(v1 + v2))
print("sub: {}".format(v1 - v2))
print("mul1: {}".format(v1*2.1))
print("mul2: {}".format(v1*v2))
print("len: {}".format(v1.len()))

print(Vector([8.462,7.893,-8.187]).cross_product(Vector([6.984,-5.975,4.778])))
