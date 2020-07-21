# 分隔链表
## 题目简述：
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

	输入: head = 1->4->3->2->5->2, x = 3
	输出: 1->2->2->4->3->5
    
具体代码：

**方法一：双指针法：时间复杂度O(n)，空间复杂度O(1):因为都是移动了原有的节点，没有使用额外的新空间**

	# Definition for singly-linked list.
	# class ListNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	
	class Solution:
	    def partition(self, head: ListNode, x: int) -> ListNode:
	        # 创建左右两个头结点，创建两个新链表，把小于x的放左链表，大于等于的放后边链表，再将两个链表进行连接
	        res_left = left = ListNode(0)
	        res_right = right = ListNode(0)
	        while head != None:
	            if head.val < x:
	                left.next = ListNode(head.val)
	                left = left.next
	            else:
	                right.next = ListNode(head.val)
	                right = right.next
	            head = head.next
	        left.next = res_right.next
	        return res_left.next

