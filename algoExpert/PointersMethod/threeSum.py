def threeNumberSum(array, targetSum):
    '''
    My solution, with help from hint
    O(n^2) runtime
    O(n) space because we have to store the numbers for the output
    '''
    array.sort()
    s = len(array)
    output = []
    for i in range(s):
        l = i+1
        r = s-1
        while(l < r):
            if targetSum > array[i] + array[l] + array[r]:
                l += 1
            elif targetSum < array[i] + array[l] + array[r]:
                r -= 1
            else:
                output.append([array[i], array[l], array[r]])
                r -= 1
                l += 1
    return output
