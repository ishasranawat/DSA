# Reverse a string 
def reverseString(str: str) -> str:
    # Split the string into words, removing extra whitespace
    words = str.split()
    
    # Reverse the list of words
    words = words[::-1]
    
    # Join the words with a single space
    return ' '.join(words)



# Palindrome 

def is_palindrome(s):
    # Convert to lowercase and remove spaces
    s = s.lower().replace(" ", "")
    
    # Check if the string is equal to its reverse
    if len(s)<=2:
        return "false"
    return "true" if s == s[::-1] else "false"
# Test the function
str = "abcdcba"
result = is_palindrome(str)
print(result)




# Reverse string including all characters
def reverseString(STR):
    return STR[::-1]

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the input string
    STR = input()
    
    # Print the reversed string
    print(reverseString(STR))


