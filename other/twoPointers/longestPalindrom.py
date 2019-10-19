'''
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.
Input: "cbbd"
Output: "bb"
'''

# Expanding from the middle 
# b   a   b   a   d
# 0 1 2 3 4 5 6 7 8
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Add space in between string
        s = ' '.join(s)
        l = len(s)
        maxL = 0
        begin, end, subL = 0, 0, 0
        
        # Define expand function
        def expand(i):
            curr_left = i-1
            curr_right = i+1
            left = right = 0
            # If character is a space then subL is 0
            if s[i] != ' ':
                subL = 1
            else: 
                subL = 0
            # Keep expanding from the midpoint (i)
            while (curr_left >= 0 and curr_right < l):
                # If the left == right
                if (s[curr_left] == s[curr_right]):
                    # If they are not a space then this is a palidrom
                    if s[curr_left] != ' ':
                        subL+=2
                    # Save the indices of left and right
                    left = curr_left
                    right = curr_right
                else:
                    break
                curr_left-=1
                curr_right+=1
            return left, right, subL
            
        # For each i as midpoint, expanding to find palindromic
        for i in range(l):
            left, right, subL = expand(i)
            # Update maxL to find the longest one
            if subL > maxL:
                maxL = subL
                begin = left
                end = right
                
        # Return the longest string without the spaces
        return s[begin:end+1].replace(' ','')
