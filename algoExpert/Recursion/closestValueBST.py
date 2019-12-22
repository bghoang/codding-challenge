def findClosestValueInBst(tree, target):
    # Write your code here.
    return helper(tree, target, float("inf"))

# O(logn) runtime
# O(n) space


def helper(node, target, closest):
    if node is None:
        return closest
    if (abs(target - node.value) < abs(target - closest)):
        closest = node.value
    if target < node.value:
        return helper(node.left, target, closest)
    else:
        return helper(node.right, target, closest)

# Optimal solution: use iteration loop through the tree and do the similar thing
# O(1) space for this method
