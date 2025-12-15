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