#11.Container with most water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        s, a = height, 0
        i = 0
        j = len(s) - 1

        while i < j:
            b = (j - i)*min(s[i], s[j])
            a = max(a, b)

            if s[i] > s[j]:
                j -= 1
            else:
                i += 1
        
        return a
#12. interger to roman
class Solution:
    def intToRoman(self, num: int) -> str:
        t = ""
        while num > 0:
            if num >= 1000:
                a = num // 1000
                t += a * 'M'
                num %= 1000

            elif num >= 100:
                b = num // 100
                if b == 9:
                     t += 'CM'
                elif  b == 4:
                     t += 'CD'
                else: 
                     t += (b // 5) * 'D' + (b % 5) * 'C'
                num %= 100

            elif num >= 10: 
                c = num // 10
                if c == 9: 
                    t += 'XC'
                elif c == 4:
                     t += 'XL'
                else: 
                    t += (c // 5) * 'L' + (c % 5) * 'X'
                num %= 10

            else:
                if num == 9: 
                    t += 'IX'
                elif num == 4: 
                    t += 'IV'
                else:
                     t += (num // 5) * 'V' + (num % 5) * 'I'
                num = 0
        
        return t
#13. roman to interger
class Solution:
    def romanToInt(self, s: str) -> int:
        t = {'CM' : 900, 'CD' : 400, 'XC' : 90, 'XL' : 40, 'IX' : 9, 'IV' : 4 }
        a = 0
        for i in t.keys():
            if i in s:
                a += t[i]
                s = s.replace(i, "")
        
        n = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}
        for i in n.keys():
            j = n[i]
            a += s.count(i) * j
        
        return a