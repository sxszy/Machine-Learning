# 环形链表
## 题目简述：
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例1:
	
	输入：head = [3,2,0,-4], pos = 1
	输出：true
	解释：链表中有一个环，其尾部连接到第二个节点。


示例2:
	
	输入：head = [1,2], pos = 0
	输出：true
	解释：链表中有一个环，其尾部连接到第一个节点。

示例3:

	输入：head = [1], pos = -1
	输出：false
	解释：链表中没有环。
    
**具体代码：**

**方法1：时间复杂度O(n)，空间复杂度O(n)**
	
	# Definition for singly-linked list.
	# class ListNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	
	class Solution:
	    def hasCycle(self, head: ListNode) -> bool:
	        """哈希表"""
	        add_set = set()
	        if head == None:
	            return False 
	        while head.next != None:
	            # 判断下一跳地址是否已经被存，代表有环，有环就直接返回了
	            if head.next in add_set:
	                return True
	            # 否则把当前节点地址加入set中
	            add_set.add(head)
	            # 切换到下一跳
	            head = head.next
	        return False

**方法2：快慢指针，有点像追及问题，时间复杂度O(n)，空间复杂度O(1)**
	# Definition for singly-linked list.
	# class ListNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	
	class Solution:
	    def hasCycle(self, head: ListNode) -> bool:
	        """快慢指针"""
	        # 空链表，或者长度为1的链表，都是无环
	        if head == None or head.next == None:
	            return False
	        # 设置初始值
	        slow = head
	        fast = head.next
	        # 开始进行循环
	        while slow != fast:
	            if fast == None or fast.next == None:
	                return False
	            slow = slow.next
	            fast = fast.next.next
	        return True