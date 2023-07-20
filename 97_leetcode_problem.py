class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2 = len(s1), len(s2)  # you get the lengths of s1 and s2
        # If the sum of lengths of s1 and s2 is not equal to the length of s3, it's not possible to interleave them
        if n1 + n2 != len(s3):
            return False
    
        # Define a recursive backtracking function with memoization using the Python's `cache` decorator
        @cache
        def back_track(i, j):
            # If both s1 and s2 are fully consumed (i reaches the length of s1 and j reaches the length of s2)
            # and the length of s3 is also exhausted, then the interleaving is successful
            if i == n1 and j == n2:
                return 1
            # Variables to store the result of choosing s1 and s2
            choose_s1 = choose_s2 = 0

            # If there are characters left in s1 and the current character in s1 matches the next character in s3
            if i < n1 and s1[i] == s3[i + j]:
                # Recursively call the backtracking function with the next character in s1 and the same character in s3
                # This represents choosing s1 for interleaving
                choose_s1 = back_track(i + 1, j)
             # If there are characters left in s2 and the current character in s2 matches the next character in s3    
            if j < n2 and s2[j] == s3[i + j]:
                # Recursively call the backtracking function with the same character in s1 and the next character in s3
                # This represents choosing s2 for interleaving
                choose_s2 = back_track(i, j + 1)
            # If either choosing s1 or choosing s2 results in successful interleaving, return True (1)
            return choose_s1 or choose_s2
        # Start the backtracking function from the beginning of s1 and s2
        return back_track(0, 0)
//i can comment now i guess
