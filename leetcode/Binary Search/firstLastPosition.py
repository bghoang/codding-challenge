'''
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Solution:
Use Binary search 2 times, 
first to find the left
second to find the right 
'''


class Solution:
    def searchRange(self, nums, target):
        l = 0
        r = len(nums) - 1
        result = [-1, -1]

        if r == -1:
            return result

        # First Binary search
        while(l < r):
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        # Check if target is found
        if nums[l] == target:
            result[0] = l
        else:
            return result

        r = len(nums) - 1

        # Second binary search
        while (l < r):
            mid = (l+r+1)//2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1

        result[1] = l
        return result
