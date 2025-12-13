#leetcode75_3/75
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        b = 0

        for i in candies:
            if i > b:
                b = i
        
        n = []
        for i in candies:
            s = i + extraCandies
            n.append(bool(s >= b))
        
        return n
#leetcode75_5/75
class Solution:
    def reverseVowels(self, s: str) -> str:

        a = 'ueoai'
        b = 'UEOAI'

        n = ""
        for i in s:
            if i in a or i in b:
             n += i
        k = n[::-1]

        c = ""
        idi = 0
        for i in s:
            if i in n:
                c += k[idi]
                idi += 1
            else:
                c += i

        return c
        