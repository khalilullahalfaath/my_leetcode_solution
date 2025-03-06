import numpy as np
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        # Initial guess (can start with x or x/2 for faster convergence)
        approx = x  

        # Iterate using Heron's method until the approximation is stable
        while True:
            better_approx = 0.5 * (approx + x / approx)
            
            # Stop when the difference is very small
            if abs(better_approx - approx) < 1e-6:
                break
            
            approx = better_approx
        
        return int(approx)  # Return the integer part as required
