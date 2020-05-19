# 最接近的三数之和
## 题目简述：
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

	例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
	
	与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

    
具体代码：
	
	class Solution:
	    def threeSumClosest(self, nums: List[int], target: int) -> int:
	        """双指针法"""
	        # 1.先对数组进行sort，时间复杂度为O(nlogn)
	        nums.sort()
	        ans = nums[0] + nums[1] + nums[2]
	        # 2.遍历数组
	        for i in range(len(nums)):
	            # 3.初始化start和end的值
	            start, end = i + 1, len(nums) - 1
	            while start < end:
	                # 4.计算和
	                sum_three = nums[start] + nums[end] + nums[i]
	                # 5.判断三数和差距是否小于上一次结果，是的话更新
	                if abs(target - sum_three) < abs(target - ans):
	                    ans = sum_three
	                # 6.判断三数和是否大于target
	                if sum_three > target:
	                    end-=1
	                elif sum_three < target:
	                    start+=1
	                # 7.相等时直接返回答案
	                else:
	                    return ans
	        return ans


**时间复杂度O(n2)，可以再优化**