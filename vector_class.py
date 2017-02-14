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
        return Vector(sum_of_vectors)

    def subtract_vectors(self, v1): 
        diff_of_vectors = [x-y for x,y in zip(self.coordinates, v1.coordinates)]
        return Vector(diff_of_vectors)

    def scalar_multiplication(self, scalar): 
        new_vector = [Decimal(scalar)*x for x in self.coordinates]
        return Vector(new_vector)

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
        """A method to determine if one vector is parallel to another"""
        return (self.is_zero() or v1.is_zero() or (self.angle_btwn_vectors(v1) == 0) or (self.angle_btwn_vectors(v1) == math.pi))

    def is_orthogonal(self, v1, limit=1E-10):
        """A method to determine if one vector is orthogonal to another.
           Because of the Decimal library, I am setting a default cut-off of 1E-15  """
        return  abs(self.dot_product(v1)) <= limit

    def is_zero(self, tolerance=1E-10): 
        """A method that determines if a vector is a zero vector or not with a default tolerance of 1E-10"""
        return self.magnitude() < tolerance

    def parallel_component(self, v1): 
        """A method that finds the projection of vector v on the basis vector self. 
           This returns a new vector of the same dimension projected onto the basis vector. """
        new_scalar = Decimal(v1.dot_product(self)) / Decimal(self.magnitude()*self.magnitude())
        projection = self.scalar_multiplication(new_scalar)
        return projection

    def find_unit_vector(self): 
        """ A method that takes a vector and returns its unit vector """
        # To do this, divide the vector coordinates by the magnitude of the vector 
        magnitude = Decimal(self.magnitude())
        unit_vector = [ point/magnitude for point in self.coordinates ]
        return Vector(unit_vector)

    def orthogonal_component(self, v1): 
        """A method that returns the orthogonal component, which is  
        equivalent to the vector from the tip of v1 intersecting at 90 degrees
        with the basis vector, or v1 - projection of v1 onto self (basis) """
        parallel_vector = self.parallel_component(v1)
        orthogonal_vector = v1.subtract_vectors(parallel_vector)
        return orthogonal_vector

    def decompose_vector(self, basis_vector): 
        """ A method that decomposes a vector, self, in relation to the basis_vector 
        by returning the parallel and orthogonal vectors"""
        vector_parallel = basis_vector.parallel_component(self)
        vector_orthogonal = basis_vector.orthogonal_component(self)
        print "parallel", vector_parallel
        print "orthogonal", vector_orthogonal
        return (vector_parallel, vector_orthogonal)

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

