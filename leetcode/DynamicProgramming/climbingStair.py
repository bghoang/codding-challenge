'''
            6  steps
use 1 step / \\ use 2 steps
          5 + 4
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        # First optimal soluton with dp table
        '''
        # Return base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize dp array with base cases
        dp = [0]*(n+1)
        # 1 step => 1 way
        dp[1] = 1
        # 2 steps => 2 ways
        dp[2] = 2

        # For other step, reduce to 2 base cases
        # dp[n] = dp[n-1] + dp[n-2]
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n]
        '''

        # More optimal case where you do not need the dp table

        if n == 1:
            return 1
        if n == 2:
            return 2
        firstStep = 1
        secondStep = 2
        for _ in range(3, n+1):
            currentStep = firstStep + secondStep
            firstStep = secondStep
            secondStep = currentStep

        return secondStep
