#!/usr/bin/env python
# _*_coding:utf-8_*_

__author__ = 'Sheng Chen'


def bubble_sort(list_a):
    for i in range(len(list_a) - 1):
        for j in range(len(list_a)-i-1):
            if list_a[j] > list_a[j+1]:
                list_a[j], list_a[j+1] = list_a[j+1], list_a[j]
    return list_a


def selection_sort(list_a):
    if not list_a:
        return []
    for i in range(len(list_a)):
        smallest_index = i
        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[smallest_index]:
                smallest_index = j
        if i != smallest_index:
            list_a[i], list_a[smallest_index] = list_a[smallest_index], list_a[i]
    return list_a


def insertion_sort(list_a):
    for i in range(1, len(list_a)):
        value = list_a[i]
        j = i - 1
        while j >= 0:
            if value < list_a[j]:
                list_a[j+1] = list_a[j]
                list_a[j] = value
            j -= 1
        print(list_a)
    return list_a


def quick_sort(list_a, left, right):
    if left >= right:
        return list_a
    key = list_a[left]
    low = left
    high = right
    while left < right:
        while left < right and list_a[right] >= key:
            right -= 1
        list_a[left] = list_a[right]
        while left < right and list_a[left] <= key:
            left += 1
        list_a[right] = list_a[left]
    list_a[right] = key
    quick_sort(list_a, low, left-1)
    quick_sort(list_a, left+1, high)
    return list_a


class TreeNode(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BTree(object):
    def __init__(self, root=None):
        self.root = root

    def pre_order(self, tree_node=None):
        if tree_node:
            print(tree_node.data)
            self.pre_order(tree_node.left)
            self.pre_order(tree_node.right)


def tree_test():
    n1 = TreeNode(data=1)
    n2 = TreeNode(2, n1)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5, n3, n4)
    n6 = TreeNode(6, n2, n5)
    n7 = TreeNode(7, n6)
    n8 = TreeNode(8)
    root = TreeNode(0, n7, n8)
    bt = BTree(root)
    bt.pre_order(bt.root)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n += 1


if __name__ == '__main__':
    # print bubble_sort([10, 45, 1, 11, 9, 24])
    # print quick_sort([10, 45, 1, 11, 9, 24], 0, 5)
    # print insertion_sort([1, 3, 5, 7, 2, 4])
    gen = fib(25)
    print([i for i in gen])
