
#This was a problem from https://www.codewars.com/kata/5266fba01283974e720000fa

import numpy as np

def get_average(numbers):
    running_total = 0
    for num in numbers:
        running_total += num
    average = running_total/len(numbers)
    return average

def get_variance(numbers):
    average       = get_average(numbers)
    deviation_sum = 0
    for num in numbers:
        deviation_sum = deviation_sum + (num - average)**2
    return deviation_sum/len(numbers)

if __name__=="__main__":
    data = [1,2,2,3]
    print(get_variance(data))