#35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i >= target:
                return nums.index(i)
        return len(nums)
#283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in nums:
            if i != 0:
                nums[j] = i
                j += 1

        for i in range(j, len(nums)):
            nums[i] = 0

        return nums
#344. Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
        
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
#349. Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set(nums1)
        b = set(nums2)
        return list(a & b)

#321. Create Maximum Number
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        t = [] 
        a = max(0, k - len(nums2))
        while a <= min(len(nums1), k):
            m = []
            for i in range(len(nums1)):
                while m and m[-1] < nums1[i] and len(m) + (len(nums1) - i) > a:
                    m.pop()
                if len(m) < a:
                    m.append(nums1[i])
            
            b = k - a
            n = []
            for j in range(len(nums2)):
                while n and n[-1] < nums2[j] and len(n) + (len(nums2) - j) > b:
                    n.pop()
                if len(n) < b:
                    n.append(nums2[j])
            
            o = []
            p, q = 0, 0
            while p < len(m) and q < len(n):
                if m[p:] >= n[q:]:
                    o.append(m[p])
                    p += 1
                else:
                    o.append(n[q])
                    q += 1

            while p < len(m):
                o.append(m[p])
                p += 1
            while q < len(n):
                o.append(n[q])
                q += 1
            
            t.append(o)
            a += 1
    
        return max(t)