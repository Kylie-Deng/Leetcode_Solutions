from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""

        # check the index i in all the strings simultaneously
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            res += strs[0][i]

        return res