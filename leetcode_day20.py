#1876. Substrings of Size Three 
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt = 0
        t = []
        
        if len(s) < 3:
            return 0
        for i in range(3):
            t.append(s[i])
        for j in range(3, len(s)):
            if t[0] != t[1] and t[1] != t[2] and t[2] != t[0]:
                cnt += 1
            t.pop(0)
            t.append(s[j])
        if t[0] != t[1] and t[1] != t[2] and t[2] != t[0]:
            cnt += 1
        
        return cnt
#643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        a = 0
        for i in range(k):
            a += nums[i]
        
        b = a
        for i in range(k, len(nums)):
            a = a + nums[i] - nums[i - k]
            if a > b:
                b = a
        
        return b/k