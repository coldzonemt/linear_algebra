import math
from decimal import Decimal, getcontext

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

    def add_vector(self, v1): 
        sum_of_vectors = [x+y for x,y in zip(self.coordinates, v1.coordinates)]
        return sum_of_vectors

    def subtract_vectors(self, v1): 
        diff_of_vectors = [x-y for x,y in zip(self.coordinates, v1.coordinates)]
        return diff_of_vectors

    def scalar_multiplication(self, scalar): 
        new_vector = [Decimal(scalar)*x for x in self.coordinates]
        return new_vector

    def magnitude(self): 
        return math.sqrt(sum([x**2 for x in self.coordinates]))

    def normalize(self): 
        try: 
            return self.scalar_multiplication(Decimal(1.0)/self.magnitude())
        except ZeroDivisionError: 
            raise Exception('Cannot normalize the zero vector')

    def dot_product(self, v1):
        return sum([x*y for x,y in zip(self.coordinates, v1.coordinates)])

    def angle_btwn_vectors(self, v1): 
        dot_prod = self.dot_product(v1)
        mag_self = Decimal(self.magnitude())
        mag_v1 = Decimal(v1.magnitude())
        
        if dot_prod == 0: 
            return (math.pi/2, 90)
        else: 
            theta_term = dot_prod/(mag_self*mag_v1)

            theta_radians = math.acos(theta_term)
            theta_degrees = math.degrees(theta_radians)
            return (theta_radians, theta_degrees)

    def is_parallel(self, v1):
        # print self.angle_btwn_vectors(v1) 
        if self.angle_btwn_vectors(v1)[1] == 90: 
            return True
        else: 
            return False 

    def is_orthogonal(self, v1):
        # print self.dot_product(v1) 
        return self.dot_product(v1) == 0

    def is_parallel_no_merge_conflicts_please(self, v1): 
        # Get the first ratio of the coordinate points
        scalar0 = self.coordinates[0]/v1.coordinates[0]
        print "scalar0: ", scalar0
        # iterate over the rest of the points
        for point in range(1,len(self.coordinates)): 
            scalar1 = self.coordinates[point]/v1.coordinates[point]
            print "scalar1: ", scalar1
            # if at any point the ratio of the points is not the same, return false
            # note that they can be negative; but it has to be consistently negative so I should fix this. 
            if scalar0 != scalar1 and scalar0 != -scalar1: 
                return False
        return True

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

