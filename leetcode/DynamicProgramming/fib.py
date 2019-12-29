class Solution:
    def fib(self, N: int) -> int:
        if N == 1:
            return 1
        if N == 0:
            return 0

        first = 0
        second = 1

        for _ in range(2, N+1):
            total = first + second
            first = second
            second = total

        return second
