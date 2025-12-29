#392. Is Sequences
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j, n = 0, 0
        for i in s:
            while j < len(t):
                if t[j] == i:
                    n += 1
                    j += 1
                    break
                j += 1

        
        if n == len(s): return True
        else: return False