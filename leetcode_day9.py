#26.Remove Duplicates from Sorted array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k
#350.Intersection of two away
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        t = []
        for i in nums1:
            if i in nums2:
                t.append(i)
                nums2.remove(i)
        
        return t