class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        lenght = 0
        stor = {}
        for i, j in enumerate(s):
            if j in stor and stor[j] >=start:
                start = stor[j] + 1
            stor[j] = i
            lenght = max(lenght, i - start + 1)
        return lenght

        