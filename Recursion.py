# Factorial 
def factorial(n):
    if n<1:
        return ("Invalid number")
    elif n==0 or n==1:
        return 1
    else:
        return (n* factorial(n-1))

print(factorial(10))


# Fibonacci
def fibonacci(n):
    if n<0:
        return ("Invalid number")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return (fibonacci(n-1)+ fibonacci(n-2))
    
print(fibonacci(7))


# sum of positive numbers
def sumofposnum(n):
    if n < 0:
        return "Invalid number"
    elif n == 0:
        return 0
    else:
        return (n % 10) + sumofposnum(n // 10)
    
print(sumofposnum(234))



# Power 
def powerofnum(x,n):
    if n==0:
        return 1
    elif n<0:
        return ("Invalid")
    else:
        return (x*powerofnum(x,n-1))

print(powerofnum(2,6))
    
