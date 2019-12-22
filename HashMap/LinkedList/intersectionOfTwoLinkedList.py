
'''
Optimal solution:
Use a dict (hashmap), go through each element in list1, save the elements in the hashmap
Go through list2, check if there is an element that match an element in the hashmap
If there is, then return that element,
Else keep going through,
If could not find any then return null

Runtime: O(n)
Space: O(size(headA))
'''

def getIntersectionNode(headA, headB):
    d = dict()
    while headA:
        d[headA] = 1
        headA= headA.next

    while headB:
        if d.get(headB):
            return headB
        headB = headB.next

    return None
