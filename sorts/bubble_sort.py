# -*- coding: utf-8 -*-

import random

# def bubble_sort(collection):
#     length = len(collection)
#     for i in range(length-1):
#         # 若后面某一连续的元素都是排序好的，则直接退出 [***, 1, 2, 3, 4, 5, 6, 7]
#         swapped = False
#         for j in range(length-i-1):
#             if collection[j] > collection[j+1]:
#                 collection[j], collection[j+1] = collection[j+1], collection[j]
#                 swapped = True
#         if not swapped:
#             break
#     return collection


def bubble_sort(collection):
    length = len(collection)
    for i in range(length-1):
        for j in range(length-i-1):
            if collection[j] > collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]
    return collection


if __name__ == '__main__':
    array = list(range(20))
    random.shuffle(array)
    print('before:', array)
    bubble_sort(array)
    print('after:', array)
