'''
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        
        tempNode = root.left
        root.left = root.right
        root.right = tempNode
        
        return root
        
