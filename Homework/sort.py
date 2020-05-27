#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Author: zheyangshi
Date: 2020/05/14
"""
import time
import random


def quick_sort_improved(array):
    """每次选取一个基准值（默认第一个），将小的放左边，大的放右边，递归地这样取，quick_sort优化版,变成随机取"""
    array = array[:]
    if len(array) < 2:
        return array
    else:
        value = random.randint(0, len(array) - 1)
        pivot = array[value]
        new = array[:]
        new.pop(value)
        # 小于基线值的归为一类
        less = [i for i in new if i <= pivot]
        greater = [i for i in new if i > pivot]
        return quick_sort_improved(less) + [pivot] + quick_sort_improved(greater)


def bubble_sort(items, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(0, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


def bubble_sort_improved(items, comp=lambda x, y: x > y):
    """冒泡排序法优化版，正着冒泡到右边，再反着冒泡到左边，每次正反冒泡一次，都可以去掉头尾加入排序"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(0, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def main(sort_function=quick_sort_improved):
    start = time.time()
    print(sort_function([3, 6, 2, 5, 4, 7, 7, 2, 1, 2, 6, 7]))
    end = time.time()
    pass_time = start - end
    print("时间: %.5f" % pass_time, "s")


if __name__ == '__main__':
    main()
