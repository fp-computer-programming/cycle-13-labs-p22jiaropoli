# Author JRI 3/5/22

def r_max(nested_num_lst): # finds the largest number in a nested list
    max = 0 
    for number in nested_num_lst:
        if type(number) == list: # if type is a list
            number = r_max(number)
            if number > max: # if the number is greater than 0
                max = number
        else: # if number is not in a list
            if number > max:
                max = number
    return max

print(r_max([4, 6, 37, [35,36], 101, 44]))