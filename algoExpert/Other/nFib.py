def getNthFib(n):
    """
    My solution
    O(n) runtime
    O(1) space
    """
    a = [0, 1]
    if n == 0 or n == 1:
        return a[0]
    i = 2
    while i < n:
        newValue = a[0] + a[1]
        a[0] = a[1]
        a[1] = newValue
        i += 1
    return a[1]
