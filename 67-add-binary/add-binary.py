class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # convert to whole number
        index_a = len(a)
        index_b = len(b)

        # print(index_a, index_b)

        total_a = 0
        for digit in a:
            total_a += (int(digit) * (2**(index_a - 1)))
            index_a -= 1
        
        total_b = 0
        for digit in b:
            total_b += (int(digit) * (2**(index_b - 1)))
            index_b -= 1

        total = total_a + total_b

        # convert to binary
        return bin(total)[2:]

        