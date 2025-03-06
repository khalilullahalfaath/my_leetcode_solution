class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = len(digits)
        total = 0

        # get the total value
        for i in range(len(digits)): 
            total = total + (digits[i] * (10**(index-1)))
            index -= 1

        # add one
        total = total + 1

        res = [int(digit) for digit in str(total)]

        return res




        