# 删除排序数组中的重复项
## 题目简述：

给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


示例 1:
    
	给定数组 nums = [1,1,2], 
	
	函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
	
	你不需要考虑数组中超出新长度后面的元素。


示例 2：
	
	给定 nums = [0,0,1,1,1,2,2,3,3,4],
	
	函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
	
	你不需要考虑数组中超出新长度后面的元素。

---
    
**具体代码：**
	
	class Solution:
	    def removeDuplicates(self, nums: List[int]) -> int:
	        """仍然是使用双指针法"""
	        i = 0
	        for j in range(len(nums)):
	            if nums[i] != nums[j]:
	                i += 1
	                nums[i] = nums[j]
	        return i + 1


**方法一如上，直双指针法**


	class Solution:
	    def removeDuplicates(self, nums: List[int]) -> int:
	        for i in range(len(nums)-1, -1, -1):
	            if i - 1 >= 0:
	                if nums[i-1] == nums[i]:
	                    nums.pop(i)
	        return len(nums)


**方法二如上，直接进行逆序遍历，这样即使删除后也不会改变索引的顺序**
