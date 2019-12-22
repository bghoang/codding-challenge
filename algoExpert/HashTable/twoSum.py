def twoNumberSum(array, targetSum):
    '''
    Some what optimal way
    O(n) runtime cause loop through array once
    O(n) space since we save elements in a dict
    '''
    '''
    output = []
    d = dict()
    for i in range(len(array)):
        num = targetSum - array[i]
        if num in d.keys():
            output.append(array[i])
            output.append(num)
            break
        else:
            d[array[i]] = 1
    return output
    '''
    '''
    Better space but worst runtime
    O(nlogn) runtime since sorting
    O(1) space since we not saving anything
    '''
    output = []
    array.sort()
    l = len(array) - 1
    f = 0
    while (l != f):
        total = array[f] + array[l]
        if total < targetSum:
            f += 1
        elif total > targetSum:
            l -= 1
        else:
            output.append(array[f])
            output.append(array[l])
            break
    return output
