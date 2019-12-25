'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6 

Example 2:
Input: [1,2,3,4]
Output: 24
'''

'''
First solution: O(nlogn) runtime/ O(logn) space caus of sortings
Sort the array, 
Find the product of the last 3 numbers
Find the product of the first 2 numbers and the last number
Return max of those 2 product

Optimal solution: O(n) runtime/ O(1) space
Find the 3 biggest numbers and 2 smallest numbers
Loop through the list, update these numbers
Find the product of the 3 biggest numbers
Find the product of the 2 smallest numbers and the biggest number
Return max of the these 2 products
'''


def maximumProduct(nums):
    # First solution
    '''
    nums.sort()
    l = len(nums)
    if l < 3:
        return
    product1 = nums[l-1] * nums[l-2] * nums[l-3]
    product2 = nums[l-1] * nums[0] * nums[1]
    return max(product1, product2)
    '''

    max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
    min1, min2 = float('inf'), float('inf')
    for num in nums:
        if num >= max1:
            max3, max2, max1 = max2, max1, num
        elif num >= max2:
            max3, max2 = max2, num
        elif num > max3:
            max3 = num
        if num <= min1:
            min2, min1 = min1, num
        elif num < min2:
            min2 = num
    return max(max1*max2*max3, min1*min2*max1)
