# 有效的括号
## 题目简述：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
	
	输入: "()"
	输出: true  

示例 2:
	
	输入: "()[]{}"
	输出: true

示例 3:
	
	输入: "(]"
	输出: false
    
具体代码：

	class Solution:
	    def isValid(self, s: str) -> bool:
	        """使用栈进行实现，遇到未匹配的括号，就将其压入栈，如果遇到匹配，就弹出栈的最上面的值，不匹配则             False，否则继续，直至查完"""
	        # 初始化栈
	        stack = []
	        # 构建mapping
	        mapping = {')':'(', '}':'{', ']':'['}
	        # 遍历字符串
	        for char in s:
	            if char in mapping:
	            # 弹出第一个值
	                top_element = stack.pop() if stack else '#'
	                # 查看弹出来的值是否匹配
	                if mapping[char] != top_element:
	                    return False
	            else:
	                stack.append(char)
	
	        return not stack 
---
**利用了辅助栈的想法**
