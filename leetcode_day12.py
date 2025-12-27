#151. Reverse Words in a Sttring
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        t = ""
        for i in range(len(s)):
            if i == 0: t += s[i]
            else: t = s[i] + " " + t
        
        return t
#165. Compare Version Numbers
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i, j = 0, 0
        while i < len(version1) or j < len(version2):
            a, b = 0, 0

            while i < len(version1) and version1[i] != '.':
                a = a * 10 + int(version1[i])
                i += 1
            while j < len(version2) and version2[j] != '.':
                b = b * 10 + int(version2[j])
                j += 1
            
            if a < b: return -1
            if a > b: return 1
            else:
                i += 1
                j += 1
        
        return 0
#189. Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums.reverse()
        k = k % len(nums)
        a, b = nums[: k], nums[k :]
        nums[: k] = a[:: -1]
        nums[k :] = b[::-1]
        return nums
#202. Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        t = set()

        while n != 1:
            if n in t: return False
            t.add(n)

            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n //= 10
                
            n = s
        
        return True