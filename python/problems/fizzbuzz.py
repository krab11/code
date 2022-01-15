# Day 8 - Arrays & Dynamic Arrays

# Problem Description
#
# Given a positive integer A, return an array of strings with all the integers from 1 to N. But for multiples of 3 the array should have “Fizz” instead of the number. For the multiples of 5, the array should have “Buzz” instead of the number. For numbers which are multiple of 3 and 5 both, the array should have "FizzBuzz" instead of the number.
#
# Look at the example for more details.
#
#
#
# Problem Constraints
#
# 1 <= A <= 500000
#
#
#
# Input Format
#
# The first argument has the integer A.
#
#
#
# Output Format
#
# Return an array of string.
#
#
#
# Example Input
#
# Input 1:
#
#  A = 5
#
#
# Example Output
#
# Output 1:
#
#  [1 2 Fizz 4 Buzz]
#
#
# Example Explanation
#
# Explanation 1:
#
#  3 is divisible by 3 so it is replaced by "Fizz".
#  Similarly, 5 is divisible by 5 so it is replaced by "Buzz".


class Solution:
	# @param A : integer
	# @return a list of strings
	def fizzBuzz(self, A):
        str_list = []
        for i in range(1, A+1):
            if i % 15 == 0:
                str_list.append("FizzBuzz")
            elif i % 3 == 0:
                str_list.append("Fizz")
            elif i % 5 == 0:
                str_list.append("Buzz")
            else:
                str_list.append(i)
        return str_list
