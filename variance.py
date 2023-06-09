
#This was a problem from https://www.codewars.com/kata/5266fba01283974e720000fa

import numpy as np

def get_average(numbers):
    running_total = 0
    for num in numbers:
        running_total += num
    average = running_total
    return average

def get_variance(numbers):
    average       = get_average(numbers)
    deviation_sum = 0
    for num in numbers:
        deviation_sum = deviation_sum + (num - average)**2
    return deviation_sum/len(numbers)

def get_dot_product(xs, ys):
    dot_product = 0
    for x,y in zip(xs, ys):
        dot_product += x*y
    return dot_product

if __name__=="__main__":
    data = [1,2,2,3]
    print(get_variance(numbers=data))
    # THE ANSWER IS 0.5, FIX ERROR AND MAKE IT OUTPUT 0.5

    #get the standard deviation

    #THE PURPOSE OF THIS NEXT 4 LINES IS JUST TO SHOW HOW TO ITERATE THROUGH MULTIPLE VARIABLES
    a = [1,2,3]
    b = [2,4,5]

    print(get_dot_product(a,b))

    #corrupt_data = [1,2,2,"3"]
    #print(get_variance(numbers=corrupt_data))

    a = [2.1, 2.5, 3.6, 4.0]
    b = [8,   10,  12,  14 ]

    #print(get_covariance(x = a, y = b))
    # THE ANSWER IS 2.267
