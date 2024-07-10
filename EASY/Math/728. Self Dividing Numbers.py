class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            num_str = str(i)
            if '0' in num_str:
                continue
            is_self_dividing = True
            for digit in num_str:
                if i % int(digit) != 0:
                    is_self_dividing = False
                    break
            if is_self_dividing:
                ans.append(i)
        return ans