# Given a string A consisting only of lowercase characters.
# You can swap any two characters of the string A any number of times, you have to check whether it is possible to convert the string A to a palindromic string.
# Return 1 if it is possible to else return 0.


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        char_map = {}
        is_it_odd = 0
        for each in A:
            if each in char_map:
                val = char_map[each]
                char_map[each] = val + 1
            else:
                char_map[each] = 1
        for key, val in char_map.items():
            if val%2==0:
                continue
            else:
                is_it_odd = is_it_odd + 1
        if is_it_odd > 1:
            return 0
        else:
            return 1
