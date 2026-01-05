#844. Backspace String Compare
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = []
        for i in s:
            if i != "#": a.append(i)
            elif a: a.pop()
        
        b = []
        for j in t:
            if j != '#': b.append(j)
            elif b: b.pop()
        
        if a == b: return True
        return False
#870. Advantage Shuffle
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        t = [0]*len(nums1)
        nums1.sort()
        copy_nums2 = sorted([(v, i) for i, v in enumerate(nums2)], reverse = True)
        j, k = 0, len(nums1) - 1

        for v, i in copy_nums2:
            if nums1[k] > v:
                t[i] = nums1[k]
                k -= 1
            else:
                t[i] = nums1[j]
                j += 1
        
        return t
#881. Boats to Save Peoples
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        cnt = 0
        i, j = 0, len(people) - 1

        while i < j: 
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            cnt += 1
        if i == j: cnt += 1
        return cnt  