# Author JRI 3/4/22

def build_car(x1, x2, x3, x4):
    wheels = x1
    axels = x2
    doors = x3
    color = x4
    return ("The car has {0} wheels, {1} axels, {2} doors, and is {3}. ".format(wheels, axels, doors, color))
x1 = input("How many wheels does the car have? ")
x2 = input("How many axels does the car have? ")
x3 = input("How many doors does the car have? ")
x4 = input("What color is the car? ")

print(build_car(x1, x2, x3, x4))

