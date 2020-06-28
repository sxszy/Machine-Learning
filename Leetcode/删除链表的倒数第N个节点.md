# 删除链表的倒数第N个节点
## 题目简述：
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。


示例：

	给定一个链表: 1->2->3->4->5, 和 n = 2.
	
	当删除了倒数第二个节点后，链表变为 1->2->3->5.

###说明：

给定的 n 保证是有效的。

###进阶：

你能尝试使用一趟扫描实现吗？
    
具体代码：

**方法一：把所有节点存进列表，再进行索引到倒数第n个，进行删除**

	# Definition for singly-linked list.
	# class ListNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	
	class Solution:
	    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
	        listnode_list = []
	        copy = head
	        while copy is not None:
	            listnode_list.append(copy)
	            copy = copy.next
	        if len(listnode_list) <= 1:
	            return None
	        if n == 1:
	            listnode_list[-2].next = None
	        else:
	            listnode_list[-n].val = listnode_list[-n+1].val
	            listnode_list[-n].next = listnode_list[-n+1].next
	        return head