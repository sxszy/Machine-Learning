# 两数之和
## 题目简述：
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。  
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。  

示例:  

    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]


具体代码：  

### 方法一

    class Solution:
	    def twoSum(self, nums, target):
	        """
	        :type nums: List[int]
	        :type target: int
	        :rtype: List[int]
	        """
	        for num in nums:
	            remain_num = target - num
	            if remain_num in nums:
	                x = nums.index(remain_num)
	                y = nums.index(num)
	                if x != y:
	                    result = [x,y]
	                    break
	                elif x == y:
	                    nums[x] = None
	                    if remain_num in nums:
	                        y = nums.index(num)
	                        result = [x,y]
	                        break
	                else:
	                    pass
	                
	        return result

---
**需要注意的点就是对特殊情况的处理：当测出序号相等时，我们将该元素置空并重新检测一次**

### 方法二

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """一遍哈希表，在放进去前看看答案是否已经在字典里面了，
		时间复杂度O(n), 空间复杂度O(n)"""
        num_dict = {}
        for i in range(len(nums)):
            remain_num = target - nums[i]
            if remain_num in num_dict:
                return num_dict[remain_num], i
            else:
                num_dict[nums[i]] = i


