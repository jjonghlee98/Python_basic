from bisect import *

a = [ 1, 2, 2, 2, 4, 4, 8 ]

print(bisect_left(a, 3))
print(bisect_right(a, 3))
print(bisect_left(a, 2))
print(bisect_right(a, 2))

print(bisect_left(a, 0))
print(bisect_right(a, 0))

print(bisect_left(a, 10))
print(bisect_right(a, 10))
