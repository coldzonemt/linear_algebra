"""
Test info for the Vector Class
"""

from vector_class import Vector 

v1 = Vector([7.579, -7.88])
w1 = Vector([22.737, 23.64])

v2 = Vector([-2.029, 9.97, 4.172])
w2 = Vector([-9.231, -6.639, -7.245])

v3 = Vector([-2.328, -7.284, -1.214])
w3 = Vector([-1.821, 1.072, -2.94])

v4= Vector([0, 0])
w4 = Vector([2.118, 4.827])

print v1.is_parallel(w1)
print v2.is_parallel(w2)
print v3.is_parallel(w3)
print v4.is_parallel(w4)


# v1 = Vector([7.887, 4.138])
# w1 = Vector([-8.802, 6.776])

# v2 = Vector([-5.955, -4.904, -1.874])
# w2 = Vector([-4.496, -8.755, 7.103])

# v3 = Vector([3.183, -7.627])
# w3 = Vector([-2.668, 5.319])

# v4= Vector([7.35, 0.221, 5.188])
# w4 = Vector([2.751, 8.259, 3.985])

# print v1.dot_product(w1)
# print v2.dot_product(w2)

# print v3.angle_btwn_vectors(w3)
# print v4.angle_btwn_vectors(w4)

# my_v = Vector([1,2,3])
# my_v1 = Vector([2,3,4])
# my_v2 = Vector([2,3,4])

# v1 = Vector([-0.221, 7.437])
# v2 = Vector([8.813, -1.331, -6.247])
# v3 = Vector([5.581, -2.136])
# v4 = Vector([1.996, 3.108, -4.554])

# print my_v1
# print my_v1 == my_v2

# print [my_v2.coordinates, my_v1.coordinates]
# print my_v.add_vector(my_v2)
# print my_v2.subtract_vectors(my_v)
# print my_v.scalar_multiplication(10)

# print v1.magnitude()
# print v2.magnitude()
# print v3.normalize()
# print v4.normalize()
