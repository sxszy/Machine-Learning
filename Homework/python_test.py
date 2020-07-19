# 生成式语法
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)

# 嵌套列表
names = ['小明', '小李', '小史', '小许']
courses = ['语文', '数学', '英语']
scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
        # 在字符串前面加上f，表示格式化输出也可以使用.format
        # 在字符串前面加上u表示unicode编码
        # ASCII只包括了英文的字符，而Unicode编码则包含了所有已知语言
        # 但是Unicode编码非常不方便，需要额外一倍的存储空间，不方便传输，
        # 所以使用utf-8这种可变长编码来传输，英文一个字节，中文三个字节
        # scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        # print(scores)

# heapq, itertools用法
"""
从列表中找出最大的或者最小的N个元素
堆结构（大根堆/小根堆）
"""
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# 可以方便找出最大最小
print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nsmallest(2, list2, key=lambda x: x['shares']))

"""
迭代工具-排列/组合/笛卡尔积
"""
import itertools

print(list(itertools.permutations('ABCD')))
print(list(itertools.combinations('ABCDE', 3)))
print(list(itertools.product('ABCD', '123')))

"""
找出序列中出现次数最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))

"""
常用算法
1.穷举法
2.贪婪法-总是选择局部最优
3.最好的选择-快速找到满意解
4.分治法-分而治之，把大问题分解为小问题
5.回溯法-按选优条件向前搜索，搜到某一步发现原先选择并不优或者达不到目标时，重新选择
6.动态规划法-把待求解问题分解成若干子问题，先求解，并保存这些子问题的解，避免产生大量重复运算
"""
# 穷举法
# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
# 假设公鸡买x只，母鸡y只，小鸡z只
for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print(x, y, z)
# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
fish = 6
while True:
    total = fish
    enough = True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        print(fish)
        break
    fish += 5

"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""
# class Thing(object):
#     """物品"""
#
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     @property
#     def value(self):
#         """价格重量比"""
#         return self.price / self.weight
#
#
# def input_thing():
#     """输入物品信息"""
#     name_str, price_str, weight_str = input().split()
#     return name_str, int(price_str), int(weight_str)
#
#
# def main():
#     """主函数"""
#     max_weight, num_of_things = map(int, input().split())
#     all_things = []
#     for _ in range(num_of_things):
#         all_things.append(Thing(*input_thing()))
#     all_things.sort(key=lambda x: x.value, reverse=True)
#     total_weight = 0
#     total_price = 0
#     # 其实就是按照价值最大的，且装的下，先拿走
#     for thing in all_things:
#         if total_weight + thing.weight <= max_weight:
#             print(f'小偷拿走了{thing.name}')
#             total_weight += thing.weight
#             total_price += thing.price
#     print(f'总价值: {total_price}美元')
#
#
# if __name__ == '__main__':
#     main()

"""
递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。
骑士巡逻：按照国际象棋骑士的走法，走遍整个棋盘的每一个方格，而且每个方格只能走一次
"""
import sys
import time

# SIZE = 5
# total = 0
#
# def print_board(board):
#     """打印棋盘"""
#     for row in board:
#         for col in row:
#             print(str(col).center(4), end='')
#         print()
#
# def patrol(board, row, col, step=1):
#     if row >= 0 and row < SIZE and \
#         col >= 0 and col < SIZE and \
#         board[row][col] == 0:
#         board[row][col] = step
#         if step == SIZE * SIZE:
#             global total
#             total += 1
#             print(f'第{total}种走法: ')
#             print_board(board)
#         patrol(board, row - 2, col - 1, step + 1)
#         board[row][col] = 0
#
#     def main():
#         board = [[0] * SIZE for _ in range(SIZE)]
#         patrol(board, SIZE - 1, SIZE - 1)
#
#     if __name__ == '__main__':
#         main()
"""
动态规划例子：子列表元素之和的最大值。

说明：子列表指的是列表中索引（下标）连续的元素构成的列表；列表中的元素是int类型，可能包含正整数、0、负整数；程序输入列表中的元素，输出子列表元素求和的最大值，例如：

输入：1 -2 3 5 -3 2

输出：8

输入：0 -2 3 5 -1 2

输出：9

输入：-9 -2 -3 -5 -3

输出：-2
"""









