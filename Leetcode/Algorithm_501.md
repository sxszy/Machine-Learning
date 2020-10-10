# 501. 二叉搜索树中的众数
## 题目简述：
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：

	给定 BST [1,null,2,2],
	
	   1
	    \
	     2
	    /
	   2
	返回[2].

提示：如果众数超过1个，不需考虑输出顺序

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

**方法一：递归：深度优先搜索**
	
	# Definition for a binary tree node.
	# class TreeNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None
	
	class Solution:
	    def findMode(self, root: TreeNode) -> List[int]:
	        """DFS"""
	        # 如果为空，直接返回
	        if not root:
	            return []
	        # 否则就设置一个计数的字典
	        count_dict = {}
	
	        def dfs(r):
	            if not r:
	                return 
	            
	            # 判断当前值是否在字典中，在的话计数加1，不在的话增加一个key，并置为1
	            if r.val not in count_dict:
	                count_dict[r.val] = 1
	            else:
	                count_dict[r.val] += 1
	            
	            # 并且遍历该节点的子节点
	            dfs(r.left)
	            dfs(r.right)
	        
	        # 然后遍历过后，去统计字典里的东西
	        dfs(root)
	        max_value = max(count_dict.values())
	        result = []
	        for key, value in count_dict.items():
	            if value == max_value:
	                result.append(key)
	        
	        return result

**方法二：广度优先搜索，时间复杂度O(n)**

	# Definition for a binary tree node.
	# class TreeNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None
	
	class Solution:
	    def findMode(self, root: TreeNode) -> List[int]:
	        import collections
	        """BFS"""
	        # 如果为空，直接返回
	        if not root:
	            return []
	        # 否则就设置一个计数的字典
	        count_dict = {}
	
	        # 设置一个队列，把root节点加入到队列中
	        deque = collections.deque()
	        deque.append(root)
	
	        # 设置while循环，退出条件是队列的长度为0
	        while len(deque) > 0:
	            x = deque.popleft()
	            if x.val not in count_dict:
	                count_dict[x.val] = 1
	            else:
	                count_dict[x.val] += 1
	
	            if x.left:
	                deque.append(x.left)
	            if x.right:
	                deque.append(x.right)
	
	        # 然后遍历过后，去统计字典里的东西
	        max_value = max(count_dict.values())
	        result = []
	        for key, value in count_dict.items():
	            if value == max_value:
	                result.append(key)
	        
	        return result

**方法三：空间复杂度O(1)**