# 删除排序链表中的重复元素 II
## 题目简述：
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

	输入: 1->2->3->3->4->4->5
	输出: 1->2->5

示例 2:

	输入: 1->1->1->2->3
	输出: 2->3
    
具体代码：

**方法一：双指针法：时间复杂度O(n)，空间复杂度O(1)**

	# Definition for singly-linked list.
	# class ListNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	
	class Solution:
	    def deleteDuplicates(self, head: ListNode) -> ListNode:
	        """双指针法"""
	        # 特殊情况
	        if not head or not head.next:
	            return head
	        # 设定指针，head为头指针，slow为慢指针，fast为快指针
	        slow = ListNode(0)
	        slow.next = head
	        head = slow
	        fast = slow.next
	        # 遍历链表
	        while fast.next != None:
	            # 如果快指针与其下一位值相同，就向右移动一位
	            if fast.val == fast.next.val:
	                fast = fast.next
	            # 否则看下快慢指针是否相邻，如果相邻就一起移动一位
	            elif slow.next == fast:
	                slow = slow.next
	                fast = fast.next
	            # 否则是中间出现重复，直接跳过
	            else:
	                fast = fast.next
	                slow.next = fast
	                
	        # 如果全部遍历完，出现slow的下一位不为fast，就把slow置为None，证明最后出现了重复
	        if slow.next != fast:
	            slow.next = None
	        return head.next


