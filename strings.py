1.## Reverse a string  ##
def reverseString(str: str) -> str:
    # Split the string into words, removing extra whitespace
    words = str.split()
    
    # Reverse the list of words
    words = words[::-1]
    
    # Join the words with a single space
    return ' '.join(words)



2.## Palindrome ##

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




3.## Reverse string including all characters ##
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


4.## FInd first non repeating character ##

from collections import Counter

def findNonRepeating(str):
    # Count the frequency of each character
    char_count = Counter(str)
    
    # Iterate over the string to find the first non-repeating character
    for char in str:
        if char_count[char] == 1:
            return char
    
    # If no non-repeating character is found, return '#'
    return '#'
# Function to process multiple test cases
def processTestCases():
    T = int(input())  # Number of test cases
    results = []
    for _ in range(T):
        string = input().strip()
        results.append(findNonRepeating(string))
    # Print all results
    print("\n".join(results))





























