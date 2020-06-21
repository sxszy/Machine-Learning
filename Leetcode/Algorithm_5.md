# 最长回文子串
## 题目简述：
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

	输入: "babad"
	输出: "bab"
	注意: "aba" 也是一个有效答案。

示例 2：
	
	输入: "cbbd"
	输出: "bb"


具体代码：

**方法一**
	
	class Solution:
	    def longestPalindrome(self, s: str) -> str:
	        """暴力法，遍历子串，并判断是否为回文子串"""
	        max = 0
	        max_s = ""
	        if len(s) <= 1:
	            return s
	        for i in range(len(s) - 1):
	            for j in range(i, len(s)):
	                tmp = s[i:j+1]
	                if tmp == tmp[::-1] and len(tmp) > max:
	                    max = len(tmp)
	                    max_s = tmp
	        return max_s

**暴力解法，复杂度高，时间复杂度O(n3)**

**方法2**

