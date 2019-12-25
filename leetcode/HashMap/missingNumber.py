'''
Find a missing number from an array contain 0,...,n elements
[0,1,3]
Missing 2
'''

'''
Brute force, sort the array
create another list go from 0 to n
compare each element in the original list with this list
return if there is a missmatch
O(nlogn) time/ O(logn) space

Better solution, using hashmap 
Loop through the list, populate the hashmap,
Loop through 0->n again checking if there any missing number
return that number

Optimal: bit manipulation
Honestly dont know how it works
'''


class Solution:
    def missingNumber(self, nums):
        # My solution
        d = dict()
        for num in nums:
            d[num] = 1
        n = 0
        l = len(nums)
        while n <= l:
            if not d.get(n):
                return n
            n += 1
        # optimal
        '''
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
        '''
