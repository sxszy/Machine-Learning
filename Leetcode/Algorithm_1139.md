# 最大的以 1 为边界的正方形
## 题目简述：
给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。

示例 1：

	输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
	输出：9

示例 2：

	输入：grid = [[1,1,0,0]]
	输出：1
    
具体代码：

**方法一：土土算**

	class Solution:
	    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
	        if len(grid) == 0 or len(grid[0]) == 0:
	            return 0
	        max_len = 0
	        m, n = len(grid), len(grid[0])
	        for i in range(m):
	            for j in range(n):
	                if grid[i][j] == 1:
	                    flag1 = True
	                    curren_max = max_len
	                    while i + curren_max < m and j +  curren_max < n:
	                        flag2 = True    
	                        # 检错左边这条边
	                        for a in range(i, i + curren_max + 1):
	                            if grid[a][j] != 1:
	                                flag1 = False
	                                break
	                        if not flag1:
	                            break
	                        # 检错上边这条边
	                        for b in range(j, j + curren_max + 1):
	                            if grid[i][b] != 1:
	                                flag1 = False
	                                break
	                        if not flag1:
	                            break
	                        # 检错右边这条边
	                        for a in range(i, i + curren_max + 1):
	                            if grid[a][j + curren_max] != 1:
	                                # 假如出现0，可以继续扩大变长再试试
	                                curren_max += 1
	                                flag2 = False
	                                break
	                        if not flag2:
	                            # 这里可以接续试试
	                            continue
	                        # 检错下边这条边
	                        for b in range(j, j + curren_max + 1):
	                            if grid[i + curren_max][b] != 1:
	                                curren_max += 1
	                                flag2 = False
	                                break
	                        if not flag2:
	                            continue
	                        curren_max += 1
	                        max_len = curren_max
	        return max_len * max_len

**方法二：动态规划**

