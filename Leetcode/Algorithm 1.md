# 两数之和
## 题目简述：
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。  

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。  

示例:
    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]

具体代码：  

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
                elif x == y:
                    nums[x] = None
                    if remain_num in nums:
                        y = nums.index(num)
                        result = [x,y]
                else:
                    pass
                
        return result
