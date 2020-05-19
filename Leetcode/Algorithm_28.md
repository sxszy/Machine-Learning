# 实现 strStr()
## 题目简述：
实现 strStr() 函数。给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。


示例 1:
    
	输入: haystack = "hello", needle = "ll"
	输出: 2

示例 2：
	
	输入: haystack = "aaaaa", needle = "bba"
	输出: -1
    
具体代码：
	
	class Solution:
	    def strStr(self, haystack: str, needle: str) -> int:
	        return haystack.find(needle)

---
**方法一如上，简单直接，但是没达到目的，直接用了内建函数**
