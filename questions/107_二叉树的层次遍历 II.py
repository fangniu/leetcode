# -*- coding: utf-8 -*-

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        values = []
        pre_row = [root]

        while len(pre_row) > 0:
            row_nodes = []
            row_values = []
            for node in pre_row:
                if node:
                    row_values.append(node.val)
                    if node.left:
                        row_nodes.append(node.left)
                    if node.right:
                        row_nodes.append(node.right)
            if len(row_values) > 0:
                values.append(row_values)
            pre_row = row_nodes
        values.reverse()
        return values
