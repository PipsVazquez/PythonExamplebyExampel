import math

print('Hi, I will have the volume of a cylinder. Please enter the radius of the circle and the depth of it')
radius = int(input())

print('Now, please enter the depth of it')
depth = int(input())

area_circle = math.pi * radius ** 2

volume_cylinder = area_circle * depth


print(round(volume_cylinder,3))