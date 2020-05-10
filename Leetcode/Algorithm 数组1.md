# 删除排序数组中的重复项
## 题目简述：
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例1:
	
	给定数组 nums = [1,1,2], 
	
	函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
	
	你不需要考虑数组中超出新长度后面的元素。

示例1:

	给定 nums = [0,0,1,1,1,2,2,3,3,4],
	
	函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
	
	你不需要考虑数组中超出新长度后面的元素。

具体代码：
	
	class Solution:
	    def removeDuplicates(self, nums: List[int]) -> int:
	        try:
	            index = 1
	            dup = nums[0]
	            while True:
	                if nums[index] == dup:
	                    nums.pop(index)
	                    continue
	                else:
	                    dup = nums[index]
	                    index += 1
	        except Exception as e:
	            return len(nums)

### 思路：设定一个指针指向当前审查位置和一个存放当前排查值的变量，如果当前值等于排查值，为重复情况，进行删除，指针不进行移动，如果当前值不等于排查值，证明之前的值排查完毕，重新赋值，而使用try,except可以捕捉到list为空，和排查完毕的情况。

优化：
