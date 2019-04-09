# -*- coding: utf-8 -*-

import random


def insertion_sort(collection):
    length = len(collection)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if collection[j-1] > collection[j]:
                collection[j-1], collection[j] = collection[j], collection[j-1]
            else:
                break


if __name__ == '__main__':
    for _ in range(5):
        array = list(range(20))
        random.shuffle(array)
        print('before:', array)
        insertion_sort(array)
        print('after:', array)
        print('=======================')
