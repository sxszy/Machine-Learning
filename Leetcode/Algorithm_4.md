# 寻找两个正序数组的中位数
## 题目描述：

给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。你可以假设 nums1 和 nums2 不会同时为空。


示例1：
    
	nums1 = [1, 3]
	nums2 = [2]

	则中位数是 2.0

示例2：
    
	nums1 = [1, 2]
	nums2 = [3, 4]
	
	则中位数是 (2 + 3)/2 = 2.5
    
具体代码：

	class Solution:
	    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
	        nums = nums1 + nums2
	        nums.sort()
	        nums_len = len(nums) 
	        zhong = nums_len // 2
	        if nums_len % 2 == 0:
	            # 偶数
	            return (nums[zhong - 1] + nums[zhong]) / 2
	        else:
	            return nums[zhong] 
        
**方法1直接将两个数组合并，根据长度为奇数还是偶数直接返回中位数**
