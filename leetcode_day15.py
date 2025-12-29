#455. Assigin Cookies
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                cnt += 1
                i += 1
            j += 1
        return cnt
#443. String Compression
class Solution:
    def compress(self, chars: List[str]) -> int:
        t = []
        cnt = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                cnt += 1

            else:
                t.append(chars[i - 1])
                if cnt > 1:
                    for j in str(cnt): t.append(j)
                cnt = 1
        t.append(chars[-1])
        
        if cnt > 1:
            for k in str(cnt): t.append(k)

        chars[:] = t
        return len(t)
#475. Heaters
from math import *
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        t, j = 0, 0

        for i in houses:
            while j < len(heaters) - 1 and abs(heaters[j] - i) >= abs(heaters[j + 1] - i):
                j += 1
            t = max(t, abs(heaters[j] - i))
        
        return t
#541. Reverse String II
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s =list(s)
        n = len(s) - 1
        
        for t in range(0, n + 1, 2*k):
            i = t
            j = min(t + k - 1, n)

            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        return "".join(s)
#524. Longest Word in Dictionary through Deleting
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        s = list(s)
        a = []
        b = []

        for t in dictionary:
            k = list(t)
            i, j = 0, 0
            while i < len(s) and j < len(k):
                if s[i] == k[j]:
                    j += 1
                i += 1
            
            if j == len(k):
                a.append(j)
                b.append(t)
        
        if a == []: return ""
        else:
            dictionary.sort()
            cd = max(int(x) for x in a)
            for c in dictionary:
                if len(c) == cd and c in b: return c