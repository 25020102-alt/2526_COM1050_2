#821. Shortest Distance to a String
from math import *
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = []

        a = -inf
        for i in range(len(s)):
            if s[i] == c:
                a = i
            n.append(i - a)
        
        b = inf
        for j in range(len(s) - 1, -1, -1):
            if s[j] == c:
                b = j
            n[j] = min(n[j], b - j)
        
        return n 
    #825. Friends of Approriate Ages
    #solution 1
    class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        cnt = 0
        left = 0
        
        if ages[-1] == ages[0] and ages[0] > 14:
            return len(ages) * (len(ages) - 1)
        for x in range(len(ages)):
            if ages[x] <= 14:
                continue
            
            while ages[left] <= 0.5 * ages[x] + 7:
                left += 1
            
            i = x + 1
            while i < len(ages) and ages[i] == ages[x]:
                i += 1

            cnt += (i - 1) - left
            
        return cnt
#solution 2
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        ans = 0
        left = 0
        right = 0
        
        for i in range(len(ages)):

            if ages[i] <= 14:
                continue
            while left < i and ages[left] <= 0.5 * ages[i] + 7:
                left += 1
            while right + 1 < len(ages) and ages[right + 1] <= ages[i]:
                right += 1

            ans += (right - left)
            
        return ans
#826. Most Profit Assigining Work
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        cnt = 0
        job = sorted(list(zip(profit, difficulty)))
        worker.sort()

        j = len(job) - 1
        for i in range(len(worker) - 1, -1, -1):
            while j >= 0:
                if job[j][1] <= worker[i]:
                    cnt += job[j][0]
                    break
                j -= 1
        
        return cnt
