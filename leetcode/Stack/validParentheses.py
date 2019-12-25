'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

Input: "([)]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        # Empty string is valid 
        if not s:
            return True
        l = len(s)
        # If length is odd then its false
        if l%2 != 0:
            return False
    
        stack = []        
        for c in s:
            # Adding openning parenthese
            if ( c == '{' or c == '[' or c == '('):
                stack.append(c)
            else: 
                # If not openning parenthese, return false
                if len(stack) == 0:
                    return False
                # Check if the first element of stack make a pair
                # with the current closing parenthese
                elif (c == '}' and stack.pop() != '{'):
                    return False        
                elif (c == ')' and stack.pop() != '('):
                    return False
                elif (c == ']' and stack.pop() != '['):
                    return False
                
        # Make sure the stack is clean
        return not stack
