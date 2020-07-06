# 从链表中删去总和值为零的连续节点
## 题目简述：
给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。

删除完毕后，请你返回最终结果链表的头节点。

 

你可以返回任何满足题目要求的答案。

（注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）

示例 1：

	输入：head = [1,2,-3,3,1]
	输出：[3,1]
	提示：答案 [1,2,1] 也是正确的。

示例 2：

	输入：head = [1,2,3,-3,4]
	输出：[1,2,4]

示例 3：

	输入：head = [1,2,3,-3,-2]  
	输出：[1]  
 
提示：

+ 给你的链表中可能有 1 到 1000 个节点。
+ 对于链表中的每个节点，节点的值：-1000 <= node.val <= 1000.
    
具体代码：
	
	# Definition for singly-linked list.
	# class ListNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	
	class Solution:
	    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
	        # 定义new为头指针
	        new = ListNode(0)
	        new.next = head
	        ListNode_dict = dict()
	        # 第一遍先把和放进字典中，允许刷新
	        # 让头指针val为0，则假如是前几个值和为0，就可以直接处理跳过
	        a = new
	        sum = 0
	        while a != None:
	            sum += a.val
	            ListNode_dict[sum] = a
	            a = a.next
	        # 第二遍检测是否和已经出现在字典中，假如是，则删去两个节点之间的所有值
	        b = new
	        sum = 0
	        while new != None:
	            sum += new.val
	            print(sum)
	            if sum in ListNode_dict.keys():
	                new.next = ListNode_dict.get(sum).next
	            new = new.next
	        return b.next