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



5. # Anagram (Modify first half to make anagram of the second half)
from collections import Counter  # This helps us count characters in a string

def minChangesToMakeAnagram(s: str) -> int:
    n = len(s)  # Get the length of the string
    
    # Split the string into two halves
    first_half = s[:n//2]  # First half
    second_half = s[n//2:]  # Second half
    
    # Count how many times each character appears in both halves
    count_first = Counter(first_half)   # Count for first half
    count_second = Counter(second_half) # Count for second half
    
    changes_needed = 0  # Start with zero changes needed
    
    # Compare the counts of characters in both halves
    for char in count_first:  # For each character in the first half
        if count_first[char] > count_second[char]:  # If there are more characters in the first half than needed
            changes_needed += count_first[char] - count_second[char]  # Add the difference to the changes needed
    
    return changes_needed  # Return the total changes needed to make the halves anagrams

# Example usage
s = "123122"
print(minChangesToMakeAnagram(s))  # Output: 1






























