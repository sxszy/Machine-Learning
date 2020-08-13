# 连续子数组的最大和
## 题目简述：
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例:

	输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
	输出: 6
	解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


具体代码：

**方法一：动态规划，把问题分解为子问题，dp[i]是以nums[i]为结尾的连续数组之和，每一个都去比较上一个连续数组最大和即dp[i-1]+nums[i]和当前值num[i]之间的大小，并将结果更新在nums[i]中，以节约空间，时间复杂度O(n)，空间复杂度O(1)**

	class Solution:
	    def maxSubArray(self, nums: List[int]) -> int:
	        for i in range(1, len(nums)):
	            nums[i] = max(nums[i-1]+nums[i], nums[i])
	        return max(nums)

**方法二：假设，不能直接修改原数组，可以增加几个变量，循环的保存动态规划表，和当前最大值，时间复杂度和空间复杂度同上**

	class Solution:
	    def maxSubArray(self, nums: List[int]) -> int:
	        if not nums:
	            return None
	        result = dp_left = nums[0]
	        for i in range(1, len(nums)):
	            dp = max(dp_left+nums[i],nums[i])
	            result = max(result, dp)
	            dp_left = dp
	        return result

