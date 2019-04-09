# -*- coding: utf-8 -*-

import random


def quick_sort(sorting, left, right):
    if left >= right:
        return
    i = left
    j = right
    pivot = sorting[i]
    while left != right:
        while left < right and sorting[right] >= pivot:
            right -= 1
        while left < right and sorting[left] <= pivot:
            left += 1
        if left < right:
            sorting[left], sorting[right] = sorting[right],  sorting[left]
    sorting[i] = sorting[left]
    sorting[left] = pivot
    quick_sort(sorting, i, left-1)
    quick_sort(sorting, left+1, j)


if __name__ == '__main__':
    for _ in range(5):
        array = list(range(20))
        random.shuffle(array)
        print('before:', array)
        quick_sort(array, 0, len(array)-1)
        print('after:', array)
        print('=======================')
