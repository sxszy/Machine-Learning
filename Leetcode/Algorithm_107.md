# 107. 二叉树的层次遍历 II
## 题目简述：
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
    
**具体代码：**

**方法1：广度优先搜索，时间复杂度O(n)**
	
	# Definition for a binary tree node.
	# class TreeNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None
	
	class Solution:
	    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
	        """广度优先搜索"""
	        import collections
	        que = collections.deque()
	        if not root:
	            return []
	        num = 0
	        res = []
	        que.append(root)
	        while que:
	            # 对于每一层的节点，都进行遍历，将他们的值存入列表，并添加其子节点到队列中
	            tmp = []
	            for i in range(len(que)):
	                x = que.popleft()
	                # tmp中添加当前节点的值
	                tmp.append(x.val)
	                if x.left:
	                    que.append(x.left)
	                if x.right:
	                    que.append(x.right)
	            res.append(tmp)
	        res.reverse()
	        return res
            
**方法1：深度优先搜索，时间复杂度O(n)** 
                 
	# Definition for a binary tree node.
	# class TreeNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None
	
	class Solution:
	    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
	        """深度优先搜索"""
	        res = [[]]
	        self.dfs(root , 1, res)
	        if res == [[]]:
	            return []
	        else:
	            return res
	
	    def dfs(self, root, level, res):
	        # 若当前节点存在
	        if root:
	            # 保证层数与res已有列表个数相同
	            if len(res) < level:
	                res.insert(0, [])
	            res[-(level)].append(root.val)
	            self.dfs(root.left, level + 1, res)
	            self.dfs(root.right, level + 1, res)


