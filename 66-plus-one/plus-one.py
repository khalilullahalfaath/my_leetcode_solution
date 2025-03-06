class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Convert list of digits to an integer
        total = int("".join(map(str, digits))) + 1

        # Convert integer back to list of digits
        return list(map(int, str(total)))




        