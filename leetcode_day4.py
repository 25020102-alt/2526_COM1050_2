#leetcode_problem_library_solution3
class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        a = ""
        b = 0
        cnt = 0

        for i in s:
         if i not in a:
            a += i
            cnt += 1
         else:
            j = a.index(i)
            a = a[j + 1 : len(a)] + i
            cnt = len(a)
         if cnt >= b:
            b = cnt
            
        return b
#leetcode_problem_library_solution4
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        a = len(nums)

        if a % 2 == 1:
            b = (a - 1)/2
            return nums[int(b)]
        else:
            b = int(a/2)
            c = nums[b] + nums[b-1]
            return c/2