def findThreeLargestNumbers(array):
    '''
    My solution
    Runtime O(nlogn)
    Space O(1)
    '''
    array.sort()
    l = len(array)
    if l <= 3:
        return array
    output = []
    output.append(array[l-3])
    output.append(array[l-2])
    output.append(array[l-1])

    return output
