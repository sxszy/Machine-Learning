#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Author: Shi Zheyang
Date: 2020/05/14
Modified Date:2020/07/08
"""
import time
import random
from functools import wraps


def timing(func):
    """
    计时装饰器
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        装饰函数
        """
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print('[' + func.__name__ + ']used:' + str(end - start))
        return r

    return wrapper


@timing
def select_sort(item, comp=lambda x, y: x < y):
    """简单选择排序，时间复杂度O(n2)，不稳定排序"""
    array = item[:]
    # i从第一个位置遍历倒数第二个位置
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if comp(array[j], array[min_index]):
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


def quick_sort_improved(item):
    """每次选取一个基准值（默认第一个），将小的放左边，大的放右边，递归地这样取，quick_sort优化版,变成随机取
    时间复杂度O(nlogn),不稳定排序"""
    array = item[:]
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


@timing
def bubble_sort(item, comp=lambda x, y: x > y):
    """冒泡排序,O(n2)"""
    items = item[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(0, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


@timing
def bubble_sort_improved(item, comp=lambda x, y: x > y):
    """冒泡排序法优化版，正着冒泡到右边，再反着冒泡到左边，每次正反冒泡一次，都可以去掉头尾加入排序"""
    items = item[:]
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


# @timing
def merge_sort(item, comp = lambda x, y: x < y):
    """归并排序，分治法，也是O(nlogn)"""
    if len(item) < 2:
        return item[:]
    mid = len(item) // 2
    left = merge_sort(item[:mid], comp)
    right = merge_sort(item[mid:], comp)
    return merge(left, right, comp)


def merge(item1, item2, comp):
    """合并（将两个有序列表合成一个有序的列表"""
    items = []
    # 创建两个索引分别在item1和item2中移动
    index1, index2 = 0, 0
    # 不断地比较两个item的中，索引指向的值，取最小的加入合并数组当中,直到有一边已经取走所有的元素
    while index1 < len(item1) and index2 < len(item2):
        if comp(item1[index1], item2[index2]):
            items.append(item1[index1])
            index1 += 1
        else:
            items.append(item2[index2])
            index2 += 1
    items += item1[index1:]
    items += item2[index2:]
    return items


def heap_sort(item):
    """堆排序"""
    pass


def main():
    array = [3, 6, 2, 5, 4, 7, 7, 2, 1, 2, 6, 7]
    start = time.time()
    print(quick_sort_improved(array))
    end = time.time()
    print("time:", end - start)
    print(select_sort(array))
    print(bubble_sort(array))
    print(bubble_sort_improved(array))
    start = time.time()
    print(merge_sort(array))
    end = time.time()
    print("time:", end-start)

if __name__ == '__main__':
    main()