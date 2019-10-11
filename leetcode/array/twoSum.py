
"""
Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
"""
def twoSum(self, nums: List[int], target: int) -> List[int]:
    l = len(nums)
    d = dict()
    # Loop through nums
    for i in range(l):
        num1 = target - nums[i]
        # For each nums[i] check if there is another element
        # in dict d that can be add up to target
        if num1 in d.keys():
            return [d[num1], i]
        # If not, add nums[i] to dict d
        else:
            d[nums[i]] = i

