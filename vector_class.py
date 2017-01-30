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
        # consider if self is zero, so wrap in try / except with ZeroDivisionError
        return self.scalar_multiplication(1/self.magnitude())

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

my_v = Vector([1,2,3])
my_v1 = Vector([2,3,4])
my_v2 = Vector([2,3,4])

v1 = Vector([-0.221, 7.437])
v2 = Vector([8.813, -1.331, -6.247])
v3 = Vector([5.581, -2.136])
v4 = Vector([1.996, 3.108, -4.554])

# print my_v1
# print my_v1 == my_v2

# print [my_v2.coordinates, my_v1.coordinates]
# print my_v.add_vector(my_v2)
# print my_v2.subtract_vectors(my_v)
# print my_v.scalar_multiplication(10)

print v1.magnitude()
print v2.magnitude()
print v3.normalize()
print v4.normalize()
