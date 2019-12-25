"""
Given a string, find the length of the longest substring without 
repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window, using 2 pointers
        begin = end = 0
        
        # Create a hash table to save the data
        d = dict()
        l = len(s)  
        ans = 0
        
        # Iterate through the string
        while (end < l):
            # If the character is not in d yet, keep iterate
            if (s[end] not in d):
                d[s[end]] = 1
                ans = max(ans, len(d))
                end += 1
            # If it does, remove the character at begin node
            else: 
                d.pop(s[begin])
                begin+=1
            
        return ans
