# Day 5
# (16 Aug)
# : Introduction to Problem Solving
#
# Smaller and Greater
# You are given an Array A of size N.
#
# Find for how many elements, there is a strictly smaller element and a strictly greater element.
#
#
#
# Input Format
#
# Given only argument A an Array of Integers.
# Output Format
#
# Return an Integer X, i.e number of elements.
# Constraints
#
# 1 <= N <= 1e5
# 1 <= A[i] <= 1e6
# For Example
#
# Example Input:
#     A = [1, 2, 3]
#
# Example Output:
#     1
#
# Explanation:
#     only 2 have a strictly smaller and strictly greater element, 1 and 3 respectively.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        for each in A:
            try:
                if each > high:
                    high = each
            except NameError:
                high = each
            try:
                if each < low:
                    low = each
            except NameError:
                low = each
        if high == low:
            return 0

        count = 0
        for each in A:
            if each != high and each != low:
                count += 1
        return count
