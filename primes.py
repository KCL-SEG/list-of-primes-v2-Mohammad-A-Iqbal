"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num%i) == 0:
                return False
        return True
    else:
        return False

def primes(number_of_primes):
    if number_of_primes < 1:
        return "ValueError"
    
    list = []

    j = 0
    
    while len(list) < (number_of_primes):
        if check_prime(j):
            list.append(j)
        
        j = j+1

              
    return list


print(primes(-5))
