# 寻找重复数
## 题目简述：
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。


示例1:
	
	输入: [1,3,4,2,2]
	输出: 2

示例2:
	
	输入: [3,1,3,4,2]
	输出: 3

说明：

1. 不能更改原数组（假设数组是只读的）。
2. 只能使用额外的 O(1) 的空间。
3. 时间复杂度小于 O(n2) 。
4. 数组中只有一个重复的数字，但它可能不止重复出现一次。

    
具体代码：
	
	class Solution:
	    def findDuplicate(self, nums: List[int]) -> int:
	        while left < right:
	            # 计算mid值
	            mid = left + (right - left) // 2
	            cnt = 0
	            for num in nums:
	                if num <= mid:
	                    cnt += 1
	            
	            if cnt <= mid:
	                # 如果cnt值是小于mid，是无重复情况
	                left = mid + 1
	            else:
	                # 否则重复项存在于[left, mid]中间
	                right = mid
	        
	        return left