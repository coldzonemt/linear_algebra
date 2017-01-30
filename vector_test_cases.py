"""
Test info for the Vector Class
"""

from vector_class import Vector 

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
