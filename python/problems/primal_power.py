# Day 8 - Arrays & Dynamic Arrays
#
# Problem Description
#
# "Primal Power" of an array is defined as the count of prime numbers present in it.
#
# Given an array of integers A of length N, you have to calculate its Primal Power.
#
#
#
# Problem Constraints
#
# 1 <= N <= 103
#
# -106 <= A[i] <= 106
#
#
#
# Input Format
#
# First and only argument is an integer array A.
#
#
#
# Output Format
#
# Return the Primal Power of array A.
#
#
#
# Example Input
#
# Input 1:
#
#  A = [-6, 10, 12]
# Input 2:
#
#  A = [-11, 7, 8, 9, 10, 11]
#
#
# Example Output
#
# Output 1:
#
#  0
# Output 2:
#
#  2
#
#
# Example Explanation
#
# Explanation 1:
#
#  -6 is not a prime number, as prime numbers are always natural numbers(by definition).
#   Also, both 10 and 12 are composite numbers.
# Explanation 2:
#
#  7 and 11 are prime numbers. Hence, Primal Power = 2.

from math import sqrt
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        for each in A:
            prime=True
            if each<=1:
                continue
            for i in range(2, int(sqrt(each) + 1)):
                if each % i == 0:
                    prime=False
                    break
            if not prime:
                continue
            count += 1
        return count
