# Author JRI 3/5/22

def factorial(num):
    if num != 0: # only works if the number is not 0
        total = 1
        counter = 1 # counter set to 1
        while counter <= num:
            total *= counter
            counter += 1
        return total
    else:
        print("0 is not a valid input") 
        
# test case
print(factorial(3))
# print(factorial(0))