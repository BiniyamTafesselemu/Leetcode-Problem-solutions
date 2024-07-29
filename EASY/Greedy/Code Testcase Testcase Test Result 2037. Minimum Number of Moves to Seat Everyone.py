class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        result=0
        students.sort()
        seats.sort()
        for i in range(len(students)):
            result += abs(seats[i]-students[i])
        return result