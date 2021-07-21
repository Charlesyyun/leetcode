'''
剑指 Offer 26. 树的子结构
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：

0 <= 节点个数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A==None or B==None: return False
        def match(A,B): # 判断以A为根节点的树是否包含B树
            if B==None: return True # 依次匹配A树和B树，如果B树已空，说明匹配完成
            if A==None or A.val!=B.val: return False # 如果A树已空或者A的节点值不等于B的节点值，说明匹配失败
            return match(A.left,B.left) and match(A.right,B.right) # 如果以上条件均不满足，那么继续匹配A左和B左，A右和B右

        # 匹配成功的可能性：1.A和B直接开始匹配成功；2. A的左子树和B匹配成功；3.A的右子树和B匹配成功
        return match(A,B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right,B)