#88
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = nums1[:m] 
        b = nums2[:n]
        nums = a + b
        
        n = len(nums)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_idx]:
                   min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
    
        nums1[:] = nums
#27
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k 
#26
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k
#169
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        a = len(nums)//2
        b = nums[a]
        if nums.count(b) > a:
            return b   
#121
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = 0
        j = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < j:
                j = prices[i]
            b = prices[i] - j
            if b > a:
                a = b
        
        return a