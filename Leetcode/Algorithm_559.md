# 559. N叉树的最大深度
## 题目简述：
给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。


**方法一：递归：深度优先搜索，时间复杂度O(n)，最坏空间复杂度O(n)，最好O(logn)**
	
	"""
	# Definition for a Node.
	class Node:
	    def __init__(self, val=None, children=None):
	        self.val = val
	        self.children = children
	"""
	
	class Solution:
	    def maxDepth(self, root: 'Node') -> int:
	        """递归"""
	        # 假如节点为空
	        if not root:
	            return 0
	        # 如果没有子节点，就记深度为1
	        elif root.children == []:
	            return 1
	        else:
	            height = [self.maxDepth(c) for c in root.children]
	        return max(height) + 1

**方法二：广度优先搜索，时间复杂度O(n)**

	"""
	# Definition for a Node.
	class Node:
	    def __init__(self, val=None, children=None):
	        self.val = val
	        self.children = children
	"""
	
	class Solution:
	    def maxDepth(self, root: 'Node') -> int:
	        if not root:
	            return 0
	        # 设定一个队列，包含有初始节点
	        que = [root]
	        depth = 1
	
	        while que:
	            # 遍历当前层节点
	            for i in range(len(que)):
	                # 弹出队列中的头节点
	                # 在队列中加入当前节点的非空子节点
	                x = que.pop(0)
	                for c in x.children:
	                    if c is not None:
	                        que.append(c)
	            depth += 1
	        return depth - 1
