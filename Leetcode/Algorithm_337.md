# 337. 打家劫舍 III
## 题目简述：
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

	输入: [3,2,3,null,3,null,1]
	
	     3
	    / \
	   2   3
	    \   \ 
	     3   1
	
	输出: 7 
	解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

示例 2:

	输入: [3,4,5,1,3,null,1]
	
	     3
	    / \
	   4   5
	  / \   \ 
	 1   3   1
	
	输出: 9
	解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

说明：

1. 不能更改原数组（假设数组是只读的）。
2. 只能使用额外的 O(1) 的空间。
3. 时间复杂度小于 O(n2) 。
4. 数组中只有一个重复的数字，但它可能不止重复出现一次。

    
具体代码：
	
	# Definition for a binary tree node.
	# class TreeNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None
	
	class Solution:
	    def rob(self, root: TreeNode) -> int:
	        def _rob(root):
	            if not root: return 0, 0
	            
	            ls, ln = _rob(root.left)
	            rs, rn = _rob(root.right)
	            # 一种情况是选中当前节点，则值为当前值加上未选中左子节点，以及未选中右子节点的值
	            # 另一种是不选当前节点，则值为左节点的选中和非选中情况，右节点的选中和非选中的值
	            return root.val + ln + rn, max(ls, ln) + max(rs, rn)
	
	        return max(_rob(root))
