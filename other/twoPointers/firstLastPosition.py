'''
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Set 2 pointers
        begin = end = 0
        found = 0
        l = len(nums)
        arr=[]
        
        # Iterate through the list
        for end in range(l):
            # If target is found, match begin and end position
            if nums[end] == target and found == 0:
                found = 1
                begin = end
                # If begin, end at the end of the list, add to arr
                if end == l -1:
                    arr.append(begin)
                    arr.append(end)
                    break
            # If target is found
            elif found == 1:
                # Add end, begin to arr when found a value not target
                if nums[end] != target:
                    arr.append(begin)
                    arr.append(end-1)
                    break
                # Or when end is at the end of list
                elif end == l - 1:
                    arr.append(begin)
                    arr.append(end)
                
        # If not found then just return -1,-1
        if found == 0:
            arr.append(-1)
            arr.append(-1)
            
        return arr
            
                
