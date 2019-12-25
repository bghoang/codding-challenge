'''
Use hashmap,
Loop through the list to populate the hashmap
Key: an element in list, value: how many times it repeated
Loop through the list again, start removing the node:
check if a node has a value of 2 or bigger, then remove the node
else if value is less than 1, then move to the next node

1->3
c
p

1: 1
2: 2
3: 1

O(2n) runtime
O(n) space since saving nodes in hashmap
'''

def deleteDuplicates(head):
  d = dict()

  present = head
  past = head

  while(present):
    if (d.get(present.val)):
      d[present.val] += 1
    else:
      d[present.val] = 1
    present = present.next

  present = head

  while(present):

    if d.get(present.val) >= 2 and past != present:
      past.next = present.next
      present = past.next

    elif d.get(present.val) >= 2 and past == present:
      head = head.next
      present = head
      past = head

    else:
      past = present
      present = present.next

  return head
