"""
Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.
"""

def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = 0
        # Loop through the list
        while i < l:
            # If there is a 0 then remove and add it at the end
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
                # Change the len to avoid infinite loop
                l-=1
            else:
                i+=1
