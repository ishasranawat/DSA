# Factorial 
def factorial(n):
    if n<1:
        return ("Invalid number")
    elif n==0 or n==1:
        return 1
    else:
        return (n* factorial(n-1))

print(factorial(10))
