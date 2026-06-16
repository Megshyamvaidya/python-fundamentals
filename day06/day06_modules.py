# import math
# print(math.pi)
# print(math.sqrt(9))
# print(math.floor(7.89))
# print(math.ceil(4.1))

# print(math.floor(4.1))
# print(math.ceil(5.9))


# importing modules from another file
# import helper
# print(helper.greet("Megshyam"))
# print(helper.add(8,7))
# print(helper.is_even(9))
# print(helper.PI)

# second way
# from helper import *
# print(greet("Megshyam"))
# print(add(9,7))
# print(is_even(8))
# print(PI)
from math_utils import square,cube,is_prime
print(square(6))
print(cube(7))
print(is_prime(7))
print(is_prime(10))
print(is_prime(2))   
print(is_prime(1))   