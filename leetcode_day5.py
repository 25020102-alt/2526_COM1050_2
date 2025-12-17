#solution7/75
class Solution:
    def reverse(self, x: int) -> int:
        a = x
        if x < 0:
            x = -x
        
        dn = 0
        while x != 0:
            dn = dn*10 + x%10
            x //= 10
        
        if a < 0:
            dn = -dn
        
        if dn < -2**31 or dn >= 2**31:
            return 0
        else:
            return dn
