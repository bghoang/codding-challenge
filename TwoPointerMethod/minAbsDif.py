 '''
Sort the array
Get two pointer, 
first iteration, find the min dif bt 2 pointers, 
second iteration, find the pairs with the min dif
if it is equal to the min dif then add them the the result array
[1,3,4,5,6]
 i 
   s
'''
def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
    arr.sort()
    l = len(arr)
    # If there are only 2 elements then return the arr
    if l <= 2: 
        return arr
    p1 = 0
    p2 = 1
    dif = float("inf")
    output = []
    # Find min differences
    while p2 < l:
        temp = abs(arr[p1] - arr[p2])
        if temp < dif:
            dif = temp
        p1 += 1
        p2 += 1
            
    p1 = 0
    p2 = 1
    # Find the pairs that have the min differences
    while p2 < l:
        temp = abs(arr[p1] - arr[p2])
        if  temp == dif:
            output.append([arr[p1], arr[p2]])
            
        p1 += 1
        p2 += 1
    return output
        
