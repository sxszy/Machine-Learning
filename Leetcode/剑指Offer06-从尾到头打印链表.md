# 剑指 Offer 06. 从尾到头打印链表
## 题目简述：
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。


### 示例 1：

	输入：head = [1,3,2]
	输出：[2,3,1]
 

### 限制：

0 <= 链表长度 <= 10000

    
具体代码：

	# Definition for singly-linked list.
	# class ListNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	
	class Solution:
	    def reversePrint(self, head: ListNode) -> List[int]:
	        """方法一，全部保存之后，返回逆序"""
	        list = []
	        while head != None:
	            list.append(head.val)
	            head = head.next
	        return list[::-1]
	        """方法2，每次都把新的数加在最前面"""
	        list = []
	        while head != None:
	            list = [head.val] + list
	            head = head.next
	        return list
	        """回溯法"""
	        return self.reversePrint(head.next) + [head.val] if head else []
