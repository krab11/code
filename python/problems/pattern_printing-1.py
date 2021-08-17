# Day 5
# (16 Aug)
# : Introduction to Problem Solving
#
# Problem Description
#
# Print a Pattern According to The Given Value of A.
#
# Example: For A = 3 pattern looks like:
#
# 1 0 0
#
# 1 2 0
#
# 1 2 3
#
#
#
# Problem Constraints
# 1 <= A <= 1000
#
#
# Input Format
# First and only argument is an integer denoting A.
#
#
#
# Output Format
# Return a two-dimensional array where each row in the returned array represents a row in the pattern.
#
#
#
# Example Input
# Input 1:
#
#  A = 3
# Input 2:
#
#  A = 4
#
#
# Example Output
# Output :1
#
#  [
#    [1, 0, 0]
#    [1, 2, 0]
#    [1, 2, 3]
#  ]
# Output 2:
#
#  [
#    [1, 0, 0, 0]
#    [1, 2, 0, 0]
#    [1, 2, 3, 0]
#    [1, 2, 3, 4]
#  ]
#
#
# Example Explanation
# Explanation 2:
#
#
#  For A = 4 pattern looks like:
#                              1 0 0 0
#                              1 2 0 0
#                              1 2 3 0
#                              1 2 3 4
#  So we will return it as two-dimensional array.

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        res = []
        for i in range(0, A):
            twod = []
            for j in range(0, A):
                if j > i:
                    twod.append(0)
                else:
                    twod.append(j + 1)
            res.append(twod)
        return res
            
