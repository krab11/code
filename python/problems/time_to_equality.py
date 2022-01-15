# Day 8 - Arrays & Dynamic Arrays
#
# Problem Description
#
# Given an integer array A of size N. In one second you can increase the value of one element by 1.
#
# Find the minimum time in seconds to make all elements of the array equal.
#
#
# Problem Constraints
#
# 1 <= N <= 1000000
# 1 <= A[i] <= 1000
#
#
# Input Format
#
# First argument is an integer array A.
#
#
# Output Format
#
# Return an integer denoting the minimum time to make all elements equal.
#
#
# Example Input
#
# A = [2, 4, 1, 3, 2]
#
#
# Example Output
#
# 8
#
#
# Example Explanation
#
# We can change the array A = [4, 4, 4, 4, 4]. The time required will be 8 seconds.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_element = A[0]
        seconds = 0
        for each in A[1:]:
            if each > max_element:
                max_element = each
        for each in A:
            seconds += max_element - each
        return seconds
