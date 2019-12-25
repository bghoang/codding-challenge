'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
'''

'''
First solution: 
Loop through the list, search for the target,
    if nums[i] == target, return i
    else if nums[i] > target, return i as well
    else:
        keep going
If reach the end of the list without returning, meaning that
the target will be at the end of the list, return len(nums)

[1,3,5,6], 7
       i

Another solution: Binary search
start from the middle, adjust left and right pointer to find the interval 
where target can be in
'''


def searchInsert(nums, target):
    # First solution
    '''
    l = len(nums)
    for i in range(l):
        if nums[i] == target:
            return i
        elif nums[i] > target:
            return i
    return l
    '''

    # Binary search
    r = len(nums)-1
    l = 0
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid-1
    return l
