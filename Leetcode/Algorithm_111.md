# 111.二叉树的最小深度
## 题目简述：
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],
	
	    3
	   / \
	  9  20
	    /  \
	   15   7

返回它的最小深度  2.

    
**具体代码：**

**方法1：递归，时间复杂度O(n),空间复杂度O(logN)**
	
	# Definition for a binary tree node.
	# class TreeNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None
	
	class Solution:
	    def minDepth(self, root: TreeNode) -> int:
	        """递归的方法获取值"""
	        if not root:
	            return 0
	
	        if not root.left and not root.right:
	            return 1
	        
	        min_len = 10**9
	        # 返回该节点下的最小深度
	        if root.left:
	            min_len = min(self.minDepth(root.left), min_len)
	
	        if root.right:
	            min_len = min(self.minDepth(root.right), min_len)
	        # 这里记得要加1
	        return min_len + 1
                  
