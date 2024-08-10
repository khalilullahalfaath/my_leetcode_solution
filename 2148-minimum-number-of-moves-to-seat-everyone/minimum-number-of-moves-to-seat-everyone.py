class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # seats
        # 1, 3, 5
        # students
        # 2, 7, 4

        # 1st student from 2 -> 1
        # 2nd student from 7 -> 6 -> 5
        # 3rd student from 4 -> 3

        # # first sort the two arrays
        seats.sort()
        students.sort()

        min_moves = 0
        for i in range(len(seats)):
            min_moves += (abs(seats[i] - students[i]))
        
        return min_moves


        