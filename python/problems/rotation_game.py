# Day 8 - Arrays & Dynamic Arrays
#
# Problem Description
#
# You are given an integer array A and an integer B. You have to print the same array after rotating it B times towards right.
#
# NOTE: You can use extra memory.
#
#
#
# Problem Constraints
#
# 1 <= |A| <= 106
#
# 1 <= A[i] <= 109
#
# 1 <= B <= 109
#
#
#
# Input Format
#
# First line begins with an integer |A| denoting the length of array, and then |A| integers denote the array elements.
# Second line contains a single integer B
#
#
#
# Output Format
#
# Print an array of integers which is the Bth right rotation of input array A, on a separate line.
#
#
#
# Example Input
#
# Input 1:
#
#  4 1 2 3 4
#  2
# Input 2:
#
#  3 1 2 2
#  3
#
#
# Example Output
#
# Output 1:
#
#  3 4 1 2
# Output 2:
#
#  1 2 2
#
#
# Example Explanation
#
# Explanation 1:
#
#  [1,2,3,4] => [4,1,2,3] => [3,4,1,2]
#
# Explanation 2:
#
#
#  [1,2,2] => [2,1,2] => [2,2,1] => [1,2,2]

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    first_line = input().rstrip()
    arr_len, arr = int(first_line.split(' ', 1)[0]), list(map(int, first_line.split(' ', 1)[1].split(' ')))
    rotate = int(input())
    res = [None] * arr_len
    if rotate == arr_len:
        print(' '.join(map(str, arr)) + ' ')
        return 0
    elif rotate > arr_len:
        rotate %= arr_len
    for i, each in enumerate(arr):
        res[(i+rotate)%arr_len] = each

    print(' '.join(map(str, res)) + ' ')
    return 0

if __name__ == '__main__':
    main()
