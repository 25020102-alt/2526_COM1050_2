#problem 70
from math import *
class Solution:
    def climbStairs(self, n: int) -> int:
        cnt = 0

        for i in range(n//2 + 1):
            a = i
            b = n - 2*a
            cnt += comb(a + b, b)
        
        return cnt
#problem 119
from math import *
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cnt = []
        
        for i in range(rowIndex + 1):
            cnt.append(comb(rowIndex,i))
        
        return cnt


        