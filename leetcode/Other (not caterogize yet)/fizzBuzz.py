'''
Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''


class Solution:
    def fizzBuzz(self, n):
        i = 1
        result = [None]*n
        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                result[i-1] = "FizzBuzz"
            elif i % 3 == 0:
                result[i-1] = "Fizz"
            elif i % 5 == 0:
                result[i-1] = "Buzz"
            else:
                result[i-1] = str(i)
            i += 1
        return result
