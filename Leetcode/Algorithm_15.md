# 三数之和
## 题目简述：
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：

	给定数组 nums = [-1, 0, 1, 2, -1, -4]，
	
	满足要求的三元组集合为：
	[
	  [-1, 0, 1],
	  [-1, -1, 2]
	]


具体代码：
	
	class Solution:
	    def threeSum(self, nums: List[int]) -> List[List[int]]:
	        n = len(nums)
	        # 假如为空，或者长度不为3，直接返回空列表
	        if nums == [] or n < 3:
	           return [] 
	        # 对数组进行排序
	        nums.sort()
	        res = []
	        for i in range(n):
	            # 假如这里已经大于0，因为是有序的，后续的不可能加起来等于0，直接返回结果
	            if(nums[i]>0):
	                return res
	            # 假如相同数，结果一样，直接跳
	            if(i>0 and nums[i]==nums[i-1]):
	                continue
	            L=i+1
	            R=n-1
	            while(L<R):
	                if(nums[i]+nums[L]+nums[R]==0):
	                    res.append([nums[i],nums[L],nums[R]])
	                    while(L<R and nums[L]==nums[L+1]):
	                        L=L+1
	                    while(L<R and nums[R]==nums[R-1]):
	                        R=R-1
	                    L=L+1
	                    R=R-1
	                # 如果结果>0，就把R向左移，否则<0时移动L
	                elif(nums[i]+nums[L]+nums[R]>0):
	                    R=R-1
	                else:
	                    L=L+1
	        return res

**时间复杂度O(n2)，可以再优化**