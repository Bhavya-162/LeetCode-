class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
            
        i = 0
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n:
            return 0
            
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
            
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
                
            result = result * 10 + digit
            i += 1
            
        return sign * result
