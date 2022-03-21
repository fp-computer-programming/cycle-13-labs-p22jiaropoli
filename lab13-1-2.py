# Author JRI 3/4/22

def build_vehicle(x1, x2, x3, x4): # function defined as build_vehicle
    wheels = x1 # variables to store number of wheels, axels, doors, and the color of the vehicle
    axels = x2
    doors = x3
    color = x4
    return ("The car has {0} wheels, {1} axels, {2} doors, and is {3}. ".format(wheels, axels, doors, color)) # uses .format to make more efficient
x1 = input("How many wheels does the car have? ") # input statements each stored as seperate variables
x2 = input("How many axels does the car have? ")
x3 = input("How many doors does the car have? ")
x4 = input("What color is the car? ")

print(build_vehicle(x1, x2, x3, x4)) # prints the return of the function
