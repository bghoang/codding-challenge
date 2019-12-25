'''
First solution: O(nm) runtime cause of insert method
Go through the 2 lists, compare the 2 values
    If the nums1[f] >= nums2[s], insert at the index
    If f reach 0 then start replace nums[f] with nums[s]
    else just keep increment f by 1
nums1 = [1,2,2,3,5,6],
             f
nums2 = [2,5,6],
           s
'''

'''
Optimal solution: O(n) runtime, O(1) space
Start from the end of the 2 arrays,
    Compare values at p1 and p2 location
    If nums1[p1] < nums2[p2], nums[curr] = nums2[p2]
    If nums1[p1] > nums2[p2], nums[curr] = nums1[p1]
if n is not 0 then keep setting nums1[curr] = nums2[n]

curr = 5
nums1 = [1, 2, 3, 0, 0, 0], m = 2
               m       curr
nums2 = [2, 5, 6]       n = 2
               n    
'''


def merge(self, nums1, m, nums2, n):
    # First solution
    '''
    s = 0
    f = 0
    while (s < n):
        if nums1[f] >= nums2[s]:
            nums1.insert(f, nums2[s])
            nums1.pop()
            s += 1
            m += 1
        elif f >= m:
            nums1[f] = nums2[s]
            s += 1
        f += 1
    return nums1
    '''

    # Optimal solution
    curr = m+n-1
    m -= 1
    n -= 1

    while (m >= 0 and n >= 0):
        if nums1[m] < nums2[n]:
            nums1[curr] = nums2[n]
            curr -= 1
            n -= 1
        else:
            nums1[curr] = nums1[m]
            m -= 1
            curr -= 1

    while (n >= 0):
        nums1[curr] = nums2[n]
        n -= 1
        curr -= 1
    return nums1
