import numpy as np

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
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
        new_vector = [scalar*x for x in self.coordinates]
        return new_vector

    def magnitude(self): 
        return sum([x**2 for x in self.coordinates])**0.5

    def normalize(self): 
        try: 
            return self.scalar_multiplication(1/self.magnitude())
        except ZeroDivisionError: 
            raise Exception('Cannot normalize the zero vector')

    def dot_product(self, v1):
        return sum([x*y for x,y in zip(self.coordinates, v1.coordinates)])

    def angle_btwn_vectors(self, v1): 
        numerator = self.dot_product(v1)
        a = Vector(self.normalize())
        b = Vector(v1.normalize())
        denominator = a.dot_product(b)
        theta_term = numerator/denominator
        print "theta_term: ", theta_term
        theta = np.arccos(theta_term)
        return theta

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

