#187. Repeated DNA Sequences
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        a = set()
        b = set()

        for i in range(len(s) - 9):
            t = s[i : i + 10]

            if t not in a: a.add(t)
            else: b.add(t)
        
        return list(b)
#209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        elif max(nums) >= target: return 1
        else:
            length = []
            i = 0
            n = 0

            for j in range(len(nums)):
                n += nums[j]
                while n >= target:
                    length.append(j - i + 1)
                    n -= nums[i]
                    i += 1
        
            return min(length)
