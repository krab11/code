# Little Ponny is given an array, A, of N integers. In a particular operation, he can set any element of the array equal to -1.
# He wants your help for finding out the minimum number of operations required such that the maximum element of the resulting array is B. 
# If it is not possible then return -1.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        A.sort(reverse=True)
        for each in A:
            if each > B:
                count = count + 1
            elif each == B:
                return count
            else:
                return -1
