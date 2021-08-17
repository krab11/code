# Day 5
# (16 Aug)
# : Introduction to Problem Solving
#
# Problem Description
#
# You are given an array of integers A of size N.
# Return the difference between the maximum among all even numbers of A and the minimum among all odd numbers in A.
#
#
#
# Problem Constraints
# 2 <= N <= 1e5
# -1e9 <= A[i] <= 1e9
# There is atleast 1 odd and 1 even number in A
#
#
#
# Input Format
# The first argument given is the integer array, A.
#
#
#
# Output Format
# Return maximum among all even numbers of A - minimum among all odd numbers in A.
#
#
#
# Example Input
# Input 1:
#
#  A = [0, 2, 9]
# Input 2:
#
#  A = [5, 17, 100, 1]
#
#
# Example Output
# Output 1:
#
# -7
# Output 2:
#
# 99
#
#
# Example Explanation
# Explanation 1:
# 
# Maximum of all even numbers = 2
# Minimum of all odd numbers = 9
# ans = 2 - 9 = -7
# Explanation 2:
#
# Maximum of all even numbers = 100
# Minimum of all odd numbers = 1
# ans = 100 - 1 = 99

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        for each in A:
            if each%2==0:
                try:
                    if each > high:
                        high = each
                except NameError:
                    high = each
            else:
                try:
                    if each < low:
                        low = each
                except NameError:
                    low = each
        return high - low
