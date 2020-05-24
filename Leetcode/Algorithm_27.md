# 移除元素
## 题目简述：
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。



示例 1:
    
	给定 nums = [3,2,2,3], val = 3,
	
	函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
	
	你不需要考虑数组中超出新长度后面的元素。


示例 2：
	
	给定 nums = [0,1,2,2,3,0,4,2], val = 2,
	
	函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
	
	注意这五个元素可为任意顺序。
	
	你不需要考虑数组中超出新长度后面的元素。

    
具体代码：
	
	class Solution:
	    def removeElement(self, nums: List[int], val: int) -> int:
	        """方法1，暴力解法"""
	        for i in range(len(nums)-1, -1, -1):
	            if nums[i] == val:
	                nums.pop(i)
	        return len(nums)

---
**方法一如上，直接进行逆序遍历，这样即使删除后也不会改变索引的顺序**


	class Solution:
	    def removeElement(self, nums: List[int], val: int) -> int:
	        """方法2，双指针法"""
	        i = 0
	        for j in range(len(nums)):
	            if nums[j] != val:
	                nums[i] = nums[j]
	                i += 1
	        return i

**方法二如上，官方的双指针法，快慢指针，快指针跳过要找的值**

	class Solution:
	    def removeElement(self, nums: List[int], val: int) -> int:
	        """仍是双指针，"""
	        i = 0
	        n = len(nums)
	        while (i < n):
	            if nums[i] == val:
	                nums[i] = nums[n-1]
	                n -= 1
	            else:
	                i += 1
	        return n

**方法三如上，官方的双指针法，每次与最后一个进行交换，并减少数组长度**