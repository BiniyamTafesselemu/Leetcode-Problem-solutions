class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res=0
        if divisor >=0 and dividend >=0:
            res+= dividend//(divisor)
        elif divisor <=0 and dividend <=0:
            res+= dividend//(divisor)
        else:
            res+= (-1*(dividend//-(divisor)))
        if res <-2**31:
            return -2**31
        elif res > 2**31-1:
            return 2**31-1
        else:
            return res