# https://github.com/jackfrued/Python-100-Days/blob/master/Day16-20/16-20.Python%E8%AF%AD%E8%A8%80%E8%BF%9B%E9%98%B6.md
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
# 把O(n2)复杂度变成O(n)
# def main():
#     items = list(map(int, input().split()))
#     # overall 全局最大，partial当前最大
#     overall = partial = items[0]
#     for i in range(1, len(items)):
#         # 检查当前值和子串值哪个大，如果是前者就相当于重新起算，否则就是子串长度继续变长
#         partial = max(items[i], partial + items[i])
#         # 看看目前局部最大和全局最大那个大，大的话就进行替换
#         overall = max(partial, overall)
#     print(overall)
#
# if __name__ == '__main__':
#     main()
"""
函数和装饰器
"""
from functools import wraps
def record_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs): # *args表示多个无名参数，**kwargs表示关键字参数
        start = time.time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {time.time() - start}秒')
        return result

    return wrapper()

@record_time
def sleep_1():
    time.sleep(2)


from functools import wraps
from threading import RLock


def singleton(cls):
    """线程安全的单例装饰器"""
    instances = {}
    locker = RLock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

"""
面对对象三要素：封装、继承和多态
"""
# from abc import ABCMeta, abstractmethod
#
#
# class Employee(metaclass=ABCMeta):
#     """员工(抽象类)"""
#
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def get_salary(self):
#         """结算月薪(抽象方法)"""
#         pass
#
#
# class Manager(Employee):
#     """部门经理"""
#
#     def get_salary(self):
#         return 15000.0
#
#
# class Programmer(Employee):
#     """程序员"""
#
#     def __init__(self, name, working_hour=0):
#         self.working_hour = working_hour
#         super().__init__(name)
#
#     def get_salary(self):
#         return 200.0 * self.working_hour
#
#
# class Salesman(Employee):
#     """销售员"""
#
#     def __init__(self, name, sales=0.0):
#         self.sales = sales
#         super().__init__(name)
#
#     def get_salary(self):
#         return 1800.0 + self.sales * 0.05
#
#
# class EmployeeFactory:
#     """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""
#
#     @staticmethod
#     def create(emp_type, *args, **kwargs):
#         """创建员工"""
#         all_emp_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
#         cls = all_emp_types[emp_type.upper()]
#         return cls(*args, **kwargs) if cls else None
#
#
# def main():
#     """主函数"""
#     emps = [
#         EmployeeFactory.create('M', '曹操'),
#         EmployeeFactory.create('P', '荀彧', 120),
#         EmployeeFactory.create('P', '郭嘉', 85),
#         EmployeeFactory.create('S', '典韦', 123000),
#     ]
#     for emp in emps:
#         print(f'{emp.name}: {emp.get_salary():.2f}元')
#
#
# if __name__ == '__main__':
#     main()

# is-a关系：继承
# has-a关系：关联 / 聚合 / 合成
# use-a关系：依赖

# 对象复制
"""
异步I/O - async / await
"""
import asyncio


def num_generator(m, n):
    """指定范围的数字生成器"""
    yield from range(m, n + 1)


# 我们可以使用async修饰将普通函数和生成器函数包装成异步函数和异步生成器，await语法只能出现在通过async修饰的函数中，否则会报SyntaxError错误。
async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            print('Prime =>', i)
            primes.append(i)
        # 在协程函数中，可以通过await语法来挂起自身的协程，并等待另一个协程完成直到返回结果：
        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


def main():
    """主函数"""
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()


if __name__ == '__main__':
    main()





