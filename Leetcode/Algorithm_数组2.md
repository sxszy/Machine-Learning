# 两数之和
## 题目简述：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

	给定 nums = [2, 7, 11, 15], target = 9
	
	因为 nums[0] + nums[1] = 2 + 7 = 9
	所以返回 [0, 1]


具体代码：
	
	class Solution:
	    def twoSum(self, nums: List[int], target: int) -> List[int]:
	        for num in nums:
	            index = nums.index(num)
	            anthor = target - num
	            try:
	                anthor_index = index + nums[(index+1):].index(anthor) + 1 
	            except Exception as e:
	                continue
	            return index, anthor_index

###思路：每次计算都从查找的数右边开始找；目前时间，空间复杂度都较差，可优化