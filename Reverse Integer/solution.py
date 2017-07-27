#!/usr/bin/env python
# _*_coding:utf-8_*_

__author__ = 'Sheng Chen'


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x % 10 == 0:
            return False
        rev = 0
        y = x
        while y:
            rev = rev*10 + y % 10
            y /= 10
        return True if x == rev else False


if __name__ == '__main__':
    print Solution().isPalindrome(0)