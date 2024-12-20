# Parenthesis checker (each opening bracket should have a closing one
class Solution:
     def isParenthesisBalanced(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
           if char in mapping:
                 top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
           else:
                stack.append(char)
         return not stack

