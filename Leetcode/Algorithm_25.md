# K 个一组翻转链表
## 题目简述：
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：

	给你这个链表：1->2->3->4->5
	
	当 k = 2 时，应当返回: 2->1->4->3->5
	
	当 k = 3 时，应当返回: 3->2->1->4->5

    
具体代码：
	
	# Definition for singly-linked list.
	# class ListNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	
	class Solution:
	    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
	        hair = ListNode(0)
	        hair.next = head
	        pre = hair
	
	        while head:
	            tail = pre
	            # 取K个，进行反转，不够K个证明已经到头，直接返回hair的下一个
	            for i in range(k):
	                tail = tail.next
	                if not tail:
	                    return hair.next
	            temp = tail.next
	            head, tail = self.reverse_listnode(head, tail)
	            # 把前后链表连接上
	            pre.next = head
	            tail.next = temp
	            pre = tail
	            head = tail.next
	        
	        return hair.next
	                
	    # 翻转一个子链表，并且返回新的头与尾
	    def reverse_listnode(self, head: ListNode, tail: ListNode):
	        """迭代法，反转链表"""
	        prev = tail.next
	        p = head
	        while prev != tail:
	            temp = p.next
	            p.next = prev
	            prev = p
	            p = temp
	        return tail, head
    
    