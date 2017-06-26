# This project for sum of Primes between 1-1000
# STEPs
# 1. need find out first 1000 prime number
#   1) what is prime number? factor 1 & self
#   2) if is, add in the list
# 2. put the numbers into a list or array
# 3. sum the list
# 4. print it out
##################
from __future__ import division
number = 2
list_number = 0
list_sum = 0

def is_prime(number):
    for i in range(2,number-1,1):
        result = number % i
        if result == 0:
            return False
    return True

while list_number < 1000:
    if is_prime(number) == True:
        #print number,list_number, list_sum
        list_number = list_number + 1
        list_sum = list_sum + number
    number = number + 1
print list_sum

