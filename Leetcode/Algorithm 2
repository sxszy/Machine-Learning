# 两数相加
## 题目描述：

给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。  
你可以假设除了数字 0 之外，这两个数字都不会以零开头

    示例：
    
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
    
具体代码：

    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = n = ListNode(0)
        # 当都为非空的时候的操作
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            # 得到进位，和个位值
            carry, val = divmod(v1+v2+carry, 10) 
            # 链表增添新节点
            n.next = ListNode(val)
            n = n.next
        return root.next   
**这题重点考察的是链表的使用
