# Understand the template code wrong so did the question wrong,
# Had to look at the solution


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(V + E) runtime
    # O(V) space
    def depthFirstSearch(self, array):
        # Write your code here.
        array.append(self.name)
        for child in self.children:
            if child.name not in array:
                child.depthFirstSearch(array)
        return array
