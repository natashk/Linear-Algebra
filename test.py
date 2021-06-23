from vector import Vector
#from line import Line

v1 = Vector([1,2,3])
v2 = Vector([5,6,7])

print("sum: {}".format(v1 + v2))
print("sub: {}".format(v1 - v2))
print("mul1: {}".format(v1*2.1))
print("mul2: {}".format(v1*v2))
print("len: {}".format(v1.len()))

print(Vector([8.462,7.893,-8.187]).cross_product(Vector([6.984,-5.975,4.778])))

