"""Write a python function, nearest_palindrome()which accepts a number and
returns the nearest palindrome greater than the given number.

sample input           expected output
99                      101
1221                    1331
"""

import sys
def nearest_palindrome(num):
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
print(nearest_palindrome(99))
print(nearest_palindrome(1221))
