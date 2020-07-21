# 148. 排序链表
## 题目简述：
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

	输入: 4->2->1->3
	输出: 1->2->3->4

示例 2:

	输入: -1->5->3->4->0
	输出: -1->0->3->4->5
    
**具体代码：**

**方法1：时间复杂度O(nlogn)，空间复杂度不止**
	
	# Definition for singly-linked list.
	# class ListNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	
	class Solution:
	    def sortList(self, head: ListNode) -> ListNode:
	        # 终止条件，当前节点为None或者下个节点为None
	        if not head or not head.next:
	            return head
	        # 设定快慢指针，用来找中点
	        slow, fast = head, head.next
	        while fast and fast.next:
	            slow, fast = slow.next, fast.next.next
	        # 切断
	        mid, slow.next = slow.next, None
			# 递归地去查找左右两链表结果
	        left, right = self.sortList(head), self.sortList(mid)
			# 设定一个新的链表
	        h = res = ListNode(0)
	        while left and right:
	            if left.val < right.val:
	                h.next, left = left, left.next
	            else:
	                h.next, right = right, right.next
	            h = h.next
	        h.next = left or right
	        return res.next
                  
