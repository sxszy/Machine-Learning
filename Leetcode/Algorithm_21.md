# 合并两个有序链表
## 题目简述：
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

    示例 1:
    
    输入: 1->2->3, 1->3->4
    输出: 1->1->2->3->4->4
    
具体代码：
	
	class Solution:
	    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
	        #取出所有数，排序后，添加进列表
	        if l1 == None:
	            return l2
	        elif l2 == None:
	            return l1
	        l1_list = []
	        l2_list = []
	        while l1 != None:
	            l1_list.append(l1.val)    
	            l1 = l1.next            
	        while l2 != None:
	            l2_list.append(l2.val)
	            l2 = l2.next
	        result = l1_list + l2_list
	        result.sort()
	        print(result)
	        new = self.list_2_linknode(result)
	        return new
	
	    def list_2_linknode(self, array):
	        tem_node = ListNode()
	        node = ListNode()
	        for i  in range(len(array)):
	            if i == 0:
	                tem_node.val = array[i]
	                node = tem_node
	            else:
	                tem_node.next = ListNode(array[i])
	                tem_node = tem_node.next
			return node

---
**方法一如上，简单直接**

	class Solution:
	    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
	        if l1 is None:
	            return l2
	        elif l2 is None:
	            return l1
	        elif l1.val < l2.val:
	            l1.next = self.mergeTwoLists(l1.next, l2)
	            return l1
	        else:
	            l2.next = self.mergeTwoLists(l1, l2.next)
	            return l2

**方法二如上，递归法，代码较为简洁**  

	class Solution:
	    def mergeTwoLists(self, l1, l2):
		# maintain an unchanging reference to node ahead of the return node.
		prehead = ListNode(-1)

		prev = prehead
		while l1 and l2:
		    if l1.val <= l2.val:
			prev.next = l1
			l1 = l1.next
		    else:
			prev.next = l2
			l2 = l2.next            
		    prev = prev.next

		# exactly one of l1 and l2 can be non-null at this point, so connect
		# the non-null list to the end of the merged list.
		prev.next = l1 if l1 is not None else l2

		return prehead.next

**官方高级做法，空间复杂度O(1)**
