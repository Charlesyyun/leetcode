'''
剑指 Offer 34. 二叉树中和为某一值的路径
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 

示例:
给定如下二叉树，以及目标和 target = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
 

提示：

节点总数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        # 先写一个函数来记录所有的路径
        path = '' # 还在走的每一个路径
        paths = [] # 已经走到叶子节点的路径
        result = [] # paths中满足条件的最终路径结果
        def construct_path(root,path):
            if root: # 如果该节点不为None，加入到path
                path += str(root.val)
                if not root.left and not root.right: # 如果已经走到了叶子节点
                    paths.append(path) # 记录走完毕的该路径
                else:
                    # 如果还没走到叶子节点，继续递归
                    path += ','
                    construct_path(root.left,path)
                    construct_path(root.right,path)

        construct_path(root,path) # 调用写好的路径记录函数，将所有路径存入paths列表
        for each in paths: # 对paths列表里的每个路径（字符串格式）进行分割以及整数转换，并求和与targe比较
            each = each.split(',')
            summation = 0
            for i in range(len(each)):
                each[i] = int(each[i])
                summation += each[i]
            if summation==target:
                result.append(each)
        return result