class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        
        # Handle negative exponent by inverting x and making n positive
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n:
            if n % 2:  # If n is odd
                result *= x
            x *= x  # Square x
            n //= 2  # Divide n by 2

        return result
