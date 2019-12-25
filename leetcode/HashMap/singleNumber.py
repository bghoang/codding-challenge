'''
Given a non-empty array of integers, every element appears twice 
except for one. Find that single one.

Input: [2,2,1]
Output: 1

Solution: use hashmap to save all the numbers and its frequnecy
'''


def singleNumber(nums):
    d = dict()
    # Generate key value pair from nums
    for e in nums:
        if (e not in d):
            d[e] = 1
        else:
            d[e] += 1

    # Check in d, return key with value of 1
    for key, value in d.items():
        if value == 1:
            return key
