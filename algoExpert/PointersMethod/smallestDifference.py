'''
Brute force: loop through each output, find the differences bt
each element in the 2 outputs, return the one with the smallest result.
If one result is 0, return the 2 numbers right away.
[-1,5,10]      result = 0
  i
[26,1,17]
    j
Runtime: O(n*m)
Space: O(1)

Optimal solution: 2 pointers
sorted 2 array
loop through 1 array, compare the difference bt 2 pointers,
if the dif is 0 then return, else increase the pointer with the smaller number
keep doing the same thing until finding the min dif.
[3,10,16]
 i
[1,17,26]
    j
Runtime: O(nlogn) + O(mlogm)
Space: O(1)
'''


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    '''
    result = [0] * 2
    dif = float('inf')
    for num1 in arrayOne:
            for num2 in arrayTwo:
                    temp = abs(num1 - num2)
                    if temp == 0:
                            return [num1, num2]
                    elif temp - 0 < dif - 0:
                            dif = temp
                            result[0] = num1
                            result[1] = num2
    return result
    '''
    p1 = 0
    p2 = 0
    dif = float('inf')
    arrayOne.sort()
    arrayTwo.sort()
    output = [0] * 2
    while (p1 < len(arrayOne) and p2 < len(arrayTwo)):
        result = abs(arrayOne[p1] - arrayTwo[p2])
        if result == 0:
            return [arrayOne[p1], arrayTwo[p2]]
        elif result < dif:
            output[0] = arrayOne[p1]
            output[1] = arrayTwo[p2]
            dif = result
        if arrayOne[p1] < arrayTwo[p2]:
            p1 += 1
        elif arrayOne[p1] >= arrayTwo[p2]:
            p2 += 1
    return output
