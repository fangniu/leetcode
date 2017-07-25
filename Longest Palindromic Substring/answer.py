class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.max_len = 1
        self.longest_str = ''
        for i in range(len(s)):
            for j in range(i+2, len(s)+1):
                self.check_palindrome(s[i:j])

    def check_palindrome(self, s):
        len_s = len(s)
        if len_s == 2 and s[0] == s[1]:
            if self.max_len < 2:
                self.longest_str = s
            return
        elif len_s == 2:
            return
        if len_s % 2 == 0:
            for i in range(len_s/2, len_s):
                if s[i] != s[len_s-1-i]:
                    return
                tmp_len = (i-len_s/2+1)*2
                if self.max_len < tmp_len:
                    self.longest_str = s[len_s-1-i:i+1]
                    self.max_len = tmp_len
        else:
            for i in range(len_s/2+1, len_s):
                if s[i] != s[len_s-1-i]:
                    return
                tmp_len = (i-len_s/2)*2+1
                if self.max_len < tmp_len:
                    self.longest_str = s[len_s-1-i:i+1]
                    self.max_len = tmp_len


if __name__ == '__main__':
    so = Solution()
    so.longestPalindrome("dabaqqqqqqq")
    print so.max_len
    print so.longest_str