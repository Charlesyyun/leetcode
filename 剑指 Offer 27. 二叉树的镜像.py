'''
剑指 Offer 27. 二叉树的镜像
剑指 Offer 27. 二叉树的镜像
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1



示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]


限制：

0 <= 节点个数 <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def flip(root): # 递归函数：根节点的左右翻转
            if root==None: return root # 终止条件：如果根节点为空，直接返回
            root.left,root.right = flip(root.right),flip(root.left) # 右节点翻转后赋值给左节点，左节点翻转后赋值给右节点
            return root
        return flip(root)