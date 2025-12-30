#532. K-diff Pairs in an Array
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        s = []
        if k == 0:
            nums.sort()
            for c in range(1, len(nums)):
                if nums[c] == nums[c - 1]:
                    if nums[c] not in s:
                        cnt += 1
                        s.append(nums[c])
            return cnt
              
        else:
            for x in nums:
                if x not in s:
                    s.append(x)
            s.sort()

            for i in s:
                if (i + k) in s:
                    cnt += 1
            
            return cnt
#556.Next Greater Element III
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = []
        while n > 0:
            s.append(n % 10)
            n //= 10
        s.reverse()
        
        i = len(s) - 1
        while i > 0:
            if s[i] > s[i - 1]:
                break
            i -= 1

        if i == 0: return -1

        for j in range(len(s) - 1, i - 1, -1):
            if s[j] > s[i - 1]:
                s[i - 1], s[j] = s[j], s[i - 1]
                break
        s[i :] = reversed(s[i :])
        
        cnt = 0
        for i in s:
            cnt = cnt * 10 + i
        
        if cnt > 2**31 - 1: return -1
        else: return cnt
#557. Reverse Words in a String III 
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            t = s[i]
            s[i] = t[:: -1]
        return " ".join(s)
#567. Permutation in String
#solution 1
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s1.sort()
        for i in range(len(s2) - len(s1) + 1):
            t = s2[i: i + len(s1)]
            t = list(t)
            t.sort()
            if t == s1: return True
        return False
#solution 2
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s1.sort()
        for i in range(len(s2) - len(s1) + 1):
            t = s2[i: i + len(s1)]
            t = list(t)
            t.sort()
            if t == s1: return True
        return False
#581. Shortest Unsorted Continuous Subarray
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = nums.copy()
        nums.sort()
        if n == nums: return 0

        for i in range(len(n)):
            if n[i] != nums[i]:
                break
        
        for j in range(len(n) - 1, 0 , -1):
            if n[j] != nums[j]:
                break
        
        return j - i + 1
#633. Sum of Square Numbers
from math import *
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(sqrt(c))

        while i <= j:
            t = i**2 + j**2
            if t == c:
                return True
            elif t > c:
                j -= 1
            else: i += 1
        
        return False
#647. Palindromic Substrings
#solution 1
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        for i in range(2, len(s) + 1):
            for j in range(len(s) - i + 1):
                t = s[j : j + i]
                if t == t[:: -1]: n += 1
        
        return n
#solution 2
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = 0
        t = len(s)
        for i in range(t):

            a, b = i, i
            while a >= 0 and b < t and s[a] == s[b]:
                n += 1
                a -= 1
                b += 1
            
            a, b = i, i  + 1
            while a >= 0 and b < t and s[a] == s[b]:
                n += 1
                a -= 1
                b += 1
        
        return n
#653:
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        n = []
        def collect(node):
            if not node: return
            collect(node.left)
            n.append(node.val)
            collect(node.right)
        collect(root)

        i, j = 0, len(n) - 1
        while i < j:
            t = n[i] + n[j] - k

            if t == 0:
                return True
            elif t > 0: j -= 1
            else: i += 1
        
        return False

        

