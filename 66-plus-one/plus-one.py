class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # index = len(digits)
        # total = 0

        # # get the total value
        # for i in range(len(digits)): 
        #     total = total + (digits[i] * (10**(index-1)))
        #     index -= 1

        # # add one
        # total = total + 1

        # res = [int(digit) for digit in str(total)]

        # return res

        n = len(digits)

        # Iterate from the last digit to the first
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No carry, return early
            digits[i] = 0  # If it's 9, set to 0 and continue

        # If all digits were 9, we need to add a new digit at the beginning
        return [1] + digits




        