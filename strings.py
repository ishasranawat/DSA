# Reverse a string 
def reverseString(str: str) -> str:
    # Split the string into words, removing extra whitespace
    words = str.split()
    
    # Reverse the list of words
    words = words[::-1]
    
    # Join the words with a single space
    return ' '.join(words)
