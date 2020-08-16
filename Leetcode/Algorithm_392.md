# 392.判断子序列
## 题目简述：
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:

	s = "abc", t = "ahbgdc"
	
	返回 true.

示例 2:

	s = "axc", t = "ahbgdc"
	
	返回 false.
    
具体代码：

**方法一：直接解法，利用python string的find函数，只要每个元素在之后的序列中被找到即可正确**
	
	class Solution:
	    def isSubsequence(self, s: str, t: str) -> bool:
	        """直接解法"""
	        start = 0
	        for i in s:
	            index = t.find(i, start)
	            if index == -1:
	                return False
	            start = index+1
	        return True

**方法二：双指针法，时间复杂度O(n+m)，空间复杂度O(1)**

	class Solution:
	    def isSubsequence(self, s: str, t: str) -> bool:
	        """双指针法"""
	        m = len(s)
	        n = len(t)
	        i, j = 0, 0 
	        while i < m and j < n:
	            if s[i] == t[j]:
	                i += 1
	            j += 1
	        return i == m