class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = start = 0
        char_dict = {}
        for i in range(len(s)):
            c = s[i]
            if c in char_dict and start <= char_dict[c]:
                start = char_dict[c] + 1
            else:
                max_len = max(max_len, i - start + 1)
            char_dict[c] = i
        return max_len


if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring("dvdf")