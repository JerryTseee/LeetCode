class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # cannot use + - * /
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend
        if dividend == 0:
            return 0
        if dividend == divisor:
            return 1

        sign = 0
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1 # output sign is positive
        elif (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = 0 # output sign is negative
        
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor

        result = 0
        while(dividend >= divisor):
            result+=1
            dividend -= divisor

        if sign == 0:
            result = -result
        
        check whether it is inside the range [-2^31, 2^31 - 1]
        if -2**31 <= result and result <= 2**31-1:
            return result
        elif result > 2**31-1:
            return 2**31-1
        elif result < -2**31:
            return -2**31