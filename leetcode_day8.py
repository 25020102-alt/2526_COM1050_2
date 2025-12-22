#15. 3Sum
class Solution:
 def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = []
    if len(nums) < 3:
        return []
    
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break

        if i > 0 and nums[i] == nums[i - 1]:
                continue

        j = i + 1
        k = len(nums) - 1

        while j < k:
            s = nums[i] + nums[j] + nums[k]

            if s == 0:
                t = [nums[i],nums[j],nums[k]]
                n.append(t)
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j - 1]:
                     j += 1
                if nums[k] == nums[k + 1]:
                    k -= 1

            elif s < 0:
                j += 1
            else:
                k -= 1
    
    return n
#17. Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        t = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl',
             '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9': 'wxyz'}

        a = [""]
        for i in  digits:
            b = []
            for j in a:
                for k in t[i]:
                    b.append(j + k)
            a = b
        
        return a
#16. 3Sum Closet
from math import *
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = inf
        a = 0
        
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k] 
                b = s - target
            
                if abs(b) < n:
                    n = abs(b)
                    a = s
                
                if b ==  0: return target
                elif b < 0: j += 1
                else: k -= 1
        
        return a