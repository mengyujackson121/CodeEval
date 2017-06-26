number = 2

def is_prime(number):
    for i in range(2,number-1,1):
        result = number % i
        if result == 0:
            return False
    return True

def ReverseNumber(n, partial=0):
    return int(''.join(reversed(str(n))))

while number < 1001:
    if is_prime(number) == True and ReverseNumber(number) == number:
        result = number
    number = number + 1
print result

