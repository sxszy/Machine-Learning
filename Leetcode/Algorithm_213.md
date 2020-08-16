# 213. 打家劫舍 II
## 题目简述：

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。


示例 1:

	输入: [2,3,2]
	输出: 3
	解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2:

	输入: [1,2,3,1]
	输出: 4
	解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
	     偷窃到的最高金额 = 1 + 3 = 4 。

    
**具体代码：**

**方法1：动态规划，时间复杂度O(n)，空间复杂度O(n)**
	
	class Solution:
	    def rob(self, nums: List[int]) -> int:
	        """动态规划，时间复杂度O(n)，空间复杂度O(n)"""
	        house_number = len(nums)
	        if house_number == 0:
	            return 0
	        elif house_number == 1:
	            return nums[0]
	        elif house_number == 2:
	            return max(nums)
	        
	        # 动态规划表的计算,dp表可以复用
	        dp = [0] * house_number
	        # 不偷第一个，偷最后一个
	        dp[0] = 0
	        dp[1] = nums[1]
	        for i in range(2, house_number):
	            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
	        max_false = dp[house_number-1]
	        # 偷第一个，不偷最后一个
	        dp[0] = nums[0]
	        dp[1] = max(nums[0], nums[1])
	        for i in range(2, house_number-1):
	            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
	        max_true = dp[house_number-2]
	        # 取两个中最大的那一个返回
	        return max(max_false, max_true)
                  
**方法2：动态规划 + 滚动数组，时间复杂度O(n)，空间复杂度O(1)**

	class Solution:
	    def rob(self, nums: List[int]) -> int:
	        """动态规划，时间复杂度O(n)，空间复杂度O(1)"""
	        house_number = len(nums)
	        if house_number == 0:
	            return 0
	        elif house_number == 1:
	            return nums[0]
	        elif house_number == 2:
	            return max(nums)
	        
	        # 动态规划表的计算,分两种情况，
	        dp = [0] * house_number
	        # 不偷第一个，偷最后一个
	        before = 0
	        after = nums[1]
	        for i in range(2, house_number):
	            new = max(before + nums[i], after)
	            before, after = after, new
	        max_false = new
	        # 偷第一个，不偷最后一个
	        before = nums[0]
	        after = max(nums[0], nums[1])
	        for i in range(2, house_number-1):
	            new = max(before + nums[i], after)
	            before, after = after, new
	        max_true = max(before, after)
	        # 取两个中最大的那一个返回
	        return max(max_false, max_true)

**方法3：动态规划+滚动数组(简洁版本，把第一个到倒数第二个取出来，和第二个到最后一个取出来，两个小问题都成了198的问题，再比较结果即可)，时间复杂度O(n)，空间复杂度O(1)**
	
	class Solution:
	    def rob(self, nums: [int]) -> int:
	        def my_rob(nums):
	            cur, pre = 0, 0
	            for num in nums:
	                cur, pre = max(pre + num, cur), cur
	            return cur
	        return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]

