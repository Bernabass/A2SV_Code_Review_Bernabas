class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        #two case

        #first case
        #if it is even return it self
        if n % 2 == 0:
            return n


        #second case
        #if it is odd return 2*n
        if n % 2 != 0:
            return 2 * n