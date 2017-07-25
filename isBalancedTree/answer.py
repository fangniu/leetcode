#!/usr/bin/env python
# _*_coding:utf-8_*_


__author__ = 'Sheng Chen'


class BinaryTreeNode(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


class Solution(object):

    def get_depth(self, root):
        if root is None:
            return 0
        l_depth = self.get_depth(root.left)
        r_depth = self.get_depth(root.right)
        return max(l_depth + 1, r_depth + 1)

    def is_balanced(self, root):
        if root is None:
            return True
        l_depth = self.get_depth(root.left)
        r_depth = self.get_depth(root.right)
        dif = l_depth - r_depth
        if dif < -1 or dif > 1:
            return False
        return self.is_balanced(root.left) and self.is_balanced(root.right)

if __name__ == '__main__':
    pass
