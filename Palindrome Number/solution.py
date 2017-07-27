#!/usr/bin/env python
# _*_coding:utf-8_*_

import re

__author__ = 'Sheng Chen'


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: string
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        string = re.findall('(^[+-0]*\d+)\D*', s.strip())
        try:
            ret = int(''.join(string))
            if ret > INT_MAX:
                return INT_MAX
            elif ret < INT_MIN:
                return INT_MIN
            else:
                return ret
        except ValueError:
            return 0


if __name__ == '__main__':
    print Solution().myAtoi("  -00121abaa")