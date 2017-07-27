#!/usr/bin/env python
# _*_coding:utf-8_*_


__author__ = 'Sheng Chen'


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        while x > 0:
            ret = ret*10 + x % 10
            x /= 10
        if x < 0:
            return self.reverse(x*-1)*-1
        if ret < -2**31 or ret > 2**31:
            return 0
        return ret


if __name__ == '__main__':
    print Solution().reverse(-31111)