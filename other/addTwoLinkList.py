"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        # Check if l1 or l2 is null
        if not l1:
            return l2
        elif not l2:
            return l1

        result = prev = newList = ListNode(c)
        val1 = val2 = 0
        # Loop through
        while (l1 or l2):
            # Check if l1 is empty of not
            if not l1:
                val1 = 0
            else:
                val1 = l1.val

            # Check if l2 is empty of not
            if not l2:
                val2 = 0
            else:
                val2 = l2.val

            # Find the new val
            newVal = val1 + val2

            # Check if it bigger than 10
            if newVal > 9:
                c = 1
                newVal -= 10
            else:
                c = 0

            # Add carry to value
            newList.val = newList.val + newVal
            newList.next = ListNode(c)

            # Move to the next node
            prev = newList
            newList = newList.next
            l1 = l1.next
            l2 = l2.next

        if newList.val == 0:
            prev.next = None
        return result


# 243
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(9)

# 564
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8
