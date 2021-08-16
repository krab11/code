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
