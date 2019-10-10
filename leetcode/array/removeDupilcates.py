"""
Given a sorted array nums, remove the duplicates in-place such 
that each element appear only once and return the new length.
"""
def removeDuplicates(self, nums):
    l = len(nums)
    # Edge case when l only has 1 element
    if l < 2:
        return l

    slowStart = 0
    # Start loop with 1 to last index
    for i in range(1,l):
        # Checking backward
        # Fix value at 1 index then check the value from the next index to last
        # If not equal then move to the next index (slow_index+1)
        if nums[i] != nums[slowStart]:
            slowStart += 1
            nums[slowStart] = nums[i]

    return slowStart + 1

