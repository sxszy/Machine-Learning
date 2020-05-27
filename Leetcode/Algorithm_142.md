# 环形链表II
## 题目简述：
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

示例1:
	
	输入：head = [3,2,0,-4], pos = 1
	输出：tail connects to node index 1
	解释：链表中有一个环，其尾部连接到第二个节点。

示例2:
	
	输入：head = [1,2], pos = 0
	输出：tail connects to node index 0
	解释：链表中有一个环，其尾部连接到第一个节点。

示例3:

	输入：head = [1], pos = -1
	输出：no cycle
	解释：链表中没有环。
    
**具体代码：**

**方法1：时间复杂度O(n)，空间复杂度O(n)**
	
	# Definition for singly-linked list.
	# class ListNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	
	class Solution:
	    def detectCycle(self, head: ListNode) -> ListNode:
	        """哈希表"""
	        add_set = set()
	        if head == None:
	            return None
	        while head.next != None:
	            if  head.next in add_set:
	                return head.next
	            add_set.add(head)           
	            head = head.next
	        return None

**方法2：快慢指针，有点像追及问题，时间复杂度O(n)，空间复杂度O(1)**
