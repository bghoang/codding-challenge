'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
'''

'''
Brute force: go through the array, check if the value match 
the target, remove that value => long runtime cause of the remove method 

2 Pointers method:
set 2 pointers p1, p2 at the beginning of the list
Loop through the nums list,
If p1 meet a value that not target, nums[p2] == nums[p1] then increase p2 by 1
Keep doing that till reaching the end of the list.
Return the value of p2 
[0,1,3,0,4,0,4,2] 
               i
           s
'''


def removeElement(nums, val):
    l = len(nums)
    s = 0
    for i in range(l):
        if nums[i] != val:
            nums[s] = nums[i]
            s += 1
    return s
