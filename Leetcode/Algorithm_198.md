# 198. 打家劫舍
## 题目简述：

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：

	输入：[1,2,3,1]
	输出：4
	解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
	     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：

	输入：[2,7,9,3,1]
	输出：12
	解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
	     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

**具体代码：**

**方法1：动态规划+滚动数组，时间复杂度O(n)，空间复杂度O(1)**
	
	class Solution:
	    def rob(self, nums: List[int]) -> int:
	        """动态规划，提前算好,时间复杂度O(n)，空间复杂度O(1)"""
	        house_number = len(nums)
	        # 针对两种特殊情况进行处理：房子数量为0和为1
	        if house_number == 0:
	            return 0
	        elif house_number == 1:
	            return nums[0]
	        
	        # 以下开始正式的动态规划表计算
	        before = nums[0]
	        after = max(nums[0], nums[1])
	        if house_number == 2:
	            return after
	        for i in range(2, house_number):
	            new = max(before + nums[i], after)
	            before, after = after, new
	        
	        return new
                  

