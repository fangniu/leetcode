# -*- coding: utf-8 -*-

import random


def selection_sort(collection):
    length = len(collection)
    for i in range(length):
        min_i = i
        for j in range(i+1, length):
            if collection[j] < collection[min_i]:
                min_i = j
        collection[i], collection[min_i] = collection[min_i], collection[i]


if __name__ == '__main__':
    for _ in range(5):
        array = list(range(20))
        random.shuffle(array)
        print('before:', array)
        selection_sort(array)
        print('after:', array)
        print('=======================')
