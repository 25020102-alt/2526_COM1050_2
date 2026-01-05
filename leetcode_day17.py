#658. Find K Closest Elements
from math import *
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i, j = 0, len(arr) - 1

        while j - i >= k:
            if abs(arr[i] - x) > abs(arr[j] - x):
                i += 1
            else:
                j -= 1
        
        return arr[i : j + 1]
#696. Count Binary Substrings
#solution 1
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cnt = 0
        
        for i in range(len(s)):
            a, b = i, i + 1
            while a >= 0 and b < len(s):
                if int(s[a])== 0 and int(s[b]) == 1:
                    cnt += 1
                    a -= 1
                    b += 1
                else: break
            
            a, b = i, i + 1
            while a >= 0 and b < len(s):
                if int(s[a]) == 1 and int(s[b]) == 0:
                    cnt += 1
                    a -= 1
                    b += 1
                else: break
        
        return cnt
#solution 2
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = 0
        i = 0
        j = 1
        
        for k in range(1, len(s)):
            if s[k] == s[k - 1]:
                j += 1
            else:
                n += min(i, j)
                i = j
                j = 1
        n += min(i, j)
        
        return n
