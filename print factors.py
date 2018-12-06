import math
def print_factors(number):
    factor1 = 1
    while factor1 <= math.sqrt(number):
        remainder = number%factor1
        factor2 = number/factor1
        if remainder == 0:
            print factor1 , factor2
        factor1 = factor1+1


while True:
    a = input('what is your number:')
    int(a)
    print_factors(a)