# 回文数
## 题目简述：
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    示例 1:
    
    输入: 121
    输出: true
    
具体代码：

    class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        return str(x)[::-1] == str(x)

## 这里最重要的一点是，python中的切片方法，[::-1]可以直接将list倒序输出##
