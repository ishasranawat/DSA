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

# def powerofnum(x, n):
#     if n == 0:
#         return 1
#     elif n < 0:
#         return 1 / powerofnum(x, -n)  # Handle negative exponents
#     else:
#         return x * powerofnum(x, n - 1)

# print(powerofnum(2, 6))  # Output: 64
# print(powerofnum(2, -3))

# Product of Array
def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])

print(productOfArray([1, 2, 3]))



# Recursive range (eg- IP-6 OP- 6+5+4+3+2+1)
def recursiveRange(num):
    if num <= 0:
        return 0
    return num + recursiveRange(num - 1)


# reverse a string
def reverse(strng):
    if len(strng) <= 1:
      return strng
    return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])


# capitalize first letter
def capitalizeFirst(arr):
    result= []
    for word in arr:
        capFirst= word[0].upper()+ word[1:]
        result.append(capFirst)
    return result
 
 
arr= ['car', 'taco', 'banana']      
print(capitalizeFirst(arr))


# CAPITALIZE WORDS SOLUTION
def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])
#Another way
words = ['hello', 'world', 'python']
for word in words:
    print(word.upper())  

















































