'''
剑指 Offer 07. 重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 

限制：

0 <= 节点个数 <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return None
        if len(preorder) != len(inorder): return None

        def recur(preorder,inorder):
            if len(preorder)==0: return #终止条件
            root = preorder[0]
            rootNode = TreeNode(root) #创建根节点
            position = inorder.index(root)

            inorder_left = inorder.copy()[:position]
            inorder_right = inorder.copy()[position+1:]

            preorder_left = preorder.copy()[1:position+1]
            preorder_right = preorder.copy()[position+1:]

            node_left = recur(preorder_left,inorder_left)
            node_right = recur(preorder_right,inorder_right)

            rootNode.left = node_left
            rootNode.right = node_right

            return rootNode
        return recur(preorder,inorder)