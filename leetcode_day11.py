#28.Find the Index of the First Occurrence in a string
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i : len(needle) + i] == needle:
                return i
                
        return -1
#42. Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        t = max(height)
        k = height.index(t)
        n = 0
        
        a = height[0]
        for i in range(k):
            if height[i] > a:
                a  = height[i]
            n += a - height[i]
        
        b = height[-1]
        for j in range(len(height) - 1, k, -1):
            if height[j] > b:
                b = height[j]
            n += b - height[j]
        
        return n
#31. Next Permutation
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
              k = len(nums) - 1
              while k >= i:
                if nums[k] > nums[i - 1]:
                    nums[i - 1], nums[k] = nums[k], nums[i - 1]
                    break
                else:
                    k -= 1
              a = nums[i : ]
              a.sort()
              nums[i : ] = a
              return nums
        
        else:
            b = nums.reverse()
            return b
#75.Sort Color
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1

            while j >= 0 and nums[j] > key:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j -= 1
            
        return nums
#80. Remove Dullicates from Sorted Array 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k
#125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for i in s:
            if i.isalnum():
                a += i
        
        a = a.lower()
        b = a[:: -1]
        if a == b: return True
        else: return False