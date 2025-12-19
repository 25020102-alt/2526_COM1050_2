#34. Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = []
        if target in nums:
            a.append(nums.index(target))
        else:
            a = [-1, -1]
            return a
        nums.reverse()
        if target in nums:
            a.append(len(nums) - 1 - nums.index(target))
        return a
#81. Search in Rotated Sorted Array II
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        min,max = 0, len(nums) - 1

        while min <= max:
            mid = (min + max) // 2

            if nums[mid] == target:
                return True
            
            elif nums[min] == nums[mid] == nums[max]:
                min += 1
                max -= 1
            
            elif nums[min] <= nums[mid]:
                if nums[min] <= target <= nums[mid]:
                    max = mid - 1
                else:
                    min = mid + 1
            
            else:
                if nums[mid] <= target <= nums[max]:
                    min = mid + 1
                else:
                    max = mid - 1
        
        return False
#167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        
        while i < j:
            s = numbers[i] + numbers[j]

            if s == target:
                return [i + 1, j + 1]
            elif s < target:
                i += 1
            else:
                j -= 1
#240. Search a 2D Matrix II
 #solution 1
 class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)

        for i in range(m):
            s = matrix[i]
            n = len(s)
            a, b = 0, n - 1
    
            while a <= b:
                mid = (a + b) // 2
                if s[mid] == target:
                    return True
                elif s[mid] < target:
                    a = mid + 1
                else:
                    b = mid - 1
        
        return False
 #solution 2
 class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = 0
        n = len(matrix[0]) - 1

        while m < len(matrix) and n >= 0:
            t = matrix[m][n]

            if t == target:
                return True
            elif t > target:
                n -= 1
            else:
                m += 1
        
        return False