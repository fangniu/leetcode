#!/usr/bin/env python
# _*_coding:utf-8_*_


__author__ = 'Sheng Chen'


class Solution(object):
    def convert(self, s, num_rows):
        """
        :type s: str
        :type num_rows: int
        :rtype: str
        """
        if num_rows == 1 or num_rows >= len(s):
            return s

        L = [''] * num_rows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == num_rows - 1:
                step = -1
            index += step

        return ''.join(L)
        # return L


if __name__ == '__main__':
    print Solution().convert('qwerty', 3)