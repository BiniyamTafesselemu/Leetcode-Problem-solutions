class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Result can have at most len(num1) + len(num2) digits
        result = [0] * (len(num1) + len(num2))

        # Reverse the strings to make it easier to multiply
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                # Multiply the digits
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                # Add to the result array
                result[i + j] += product
                # Handle carry
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        # Remove leading zeros and convert to string
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return ''.join(str(x) for x in result[::-1])

