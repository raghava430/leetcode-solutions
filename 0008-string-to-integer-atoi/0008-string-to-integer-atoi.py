class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        
        # 1. Skip whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # 2. Sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # 3. Convert digits
        res = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # 4. Overflow check BEFORE adding
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            
            res = res * 10 + digit
            i += 1
        
        return sign * res