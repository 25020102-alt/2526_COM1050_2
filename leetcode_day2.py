#leetcode_problem_two sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
#leetcode75_2/75
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            
            if len(str1) % len(str2) == 0:
                return str2

            for i in range(int(len(str2)/2) + 1):
                a = str2[0 : i + 1]
                c = i + 1
                d = 2*i + 2
                b = str2[c : d]
                cnt = 1

                while b == a:
                    cnt += 1
                    c += i + 1
                    d += i + 1
                    b = str2[c : d]

                if cnt == len(str2)/len(a): 
                    return a
            
        else: return "" 