# 反转链表
## 题目简述：
反转一个单链表。

示例:

	输入: 1->2->3->4->5->NULL
	输出: 5->4->3->2->1->NULL
    
具体代码：

**方法一，迭代法，时间复杂度O(n)，空间复杂度O(1)**

	# Definition for singly-linked list.
	# class ListNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	
	class Solution:
	    def reverseList(self, head: ListNode) -> ListNode:
	        """迭代法，保存上一个和下一个值"""
	        prev = None
	        curr = head
	        while curr != None:
	            # temp保存下一个节点
	            temp = curr.next
	            # 把当前结点指向上一节点
	            curr.next = prev
	            # 然后往后移位
	            prev = curr
	            # 同时令curr为新的
	            curr = temp
	        # 返回prev，此时位置为最后头节点，curr为None
	        return prev
	
**方法二，递归法,时间复杂度O(n)，空间复杂度O(n)**

	# Definition for singly-linked list.
	# class ListNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	
	class Solution:
	    def reverseList(self, head: ListNode) -> ListNode:
	        """递归法"""
	        if head == None or head.next == None:
	            return head
	        p = self.reverseList(head.next)
	        # 让下一节点指向该节点
	        head.next.next = head
	        # 再把原本的指向断掉
	        head.next = None
	        return p