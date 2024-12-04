# Star problem
def pattern(n):
    for i in range(1,n+1):
        spaces= " " *(n-i)
        stars= "*"* (2*i-1)

        print (spaces+stars)

n=int(input())
pattern(n)

def is_prime(n):
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check for divisibility up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True
