#leetcode75_solution7/75
class Solution:
    def reverse(self, x: int) -> int:
        a = x
        if x < 0:
            x = -x
        
        dn = 0
        while x != 0:
            dn = dn*10 + x%10
            x //= 10
        
        if a < 0:
            dn = -dn
        
        if dn < -2**31 or dn >= 2**31:
            return 0
        else:
            return dn
#88.merge sort array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = nums1[:m] 
        b = nums2[:n]
        nums = a + b
        nums.sort()
        nums1[:] = nums
#217. contain deplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in nums:
            if i in a:
                return True
            else:
                a.add(i)
        return False
#242. valid anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      else:
        a = list(t)
        for i in s:
            if i in a:
                a.remove(i)
            else:
                return False
        
        if a == []:
            return True
        else:
            return False 
#169. majority element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        a = len(nums)//2
        b = nums[a]
        if nums.count(b) > a:
            return b   
