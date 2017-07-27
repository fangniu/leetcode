#!/usr/bin/env python
# _*_coding:utf-8_*_


class Solution(object):
    def longestPalindrome(self, s):
        t_s = '#' + '#'.join(s) + '#'  # 字符串处理，用特殊字符隔离字符串，方便处理偶数子串
        lens = len(t_s)
        f = []  # 辅助列表：f[i]表示i作中心的最长回文子串的长度
        maxj = 0  # 记录对i右边影响最大的字符位置j
        maxl = 0  # 记录j影响范围的右边界
        maxd = 0  # 记录最长的回文子串长度
        maxd_i = 0  # 记录最长的回文子串长度时对应的index号
        for i in range(lens):  # 遍历字符串
            if maxl > i:
                count = min(maxl - i, int(f[2 * maxj - i] / 2) + 1)  # 这里为了方便后续计算使用count，其表示当前字符到其影响范围的右边界的距离
            else:
                count = 1
            while i - count >= 0 and i + count < lens and t_s[i - count] == t_s[i + count]:  # 两边扩展
                count += 1
            if (i - 1 + count) > maxl:  # 更新影响范围最大的字符j及其右边界
                maxl, maxj = i - 1 + count, i
            f.append(count * 2 - 1)
            # maxd = max(maxd, f[i])  # 更新回文子串最长长度
            if f[i] > maxd:
                maxd = f[i]
                maxd_i = i
        ret_len = int((maxd + 1) / 2) - 1  # 去除特殊字符
        return t_s[maxd_i-ret_len:maxd_i+ret_len+1].replace('#', '')

if __name__ == '__main__':
    print Solution().longestPalindrome("cbbd")
