class Solution:
    def sumBase(self, n: int, k: int) -> int:
        total=0
        while n >= k:
            total+=n%k
            n=n//k
        return total+n
