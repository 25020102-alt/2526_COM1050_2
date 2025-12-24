#387.First Unique Character in a string
class Solution:
    def firstUniqChar(self, s: str) -> int:
        t = {}
        for i in s:
            t[i] = t.get(i, 0) + 1
        for i in t.keys():
            if t[i] == 1:
                return s.index(i)
        return -1
#27.Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k 
#121. Best time to Buy Sell Stock
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
    