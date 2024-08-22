class Solution:
    def minSteps(self, n: int) -> int:
        copy = 0
        paste = 1
        count_operations = 0

        while paste != n:

            if n % paste == 0:
                copy = paste
                count_operations += 1

            paste += copy
            count_operations += 1

        return count_operations