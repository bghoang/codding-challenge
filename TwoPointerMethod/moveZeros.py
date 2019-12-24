'''
Optimal solution: 
2 pointers method, replace nums[s] with nums[i] when nums[i] != 0
0 1 0 3 12
i
s

O(n) runtime
O(1) space

Note: know the optimal solution, having trouble implementing it
'''
def moveZeroes(nums):
    l = len(nums)
    s = 0

    if 0 is not in nums:
        return nums

    for i in range(l):
        if nums[i] != 0:
            nums[s] = nums[i]
            s+=1

    for i in range(s,l):
        nums[i] = 0
