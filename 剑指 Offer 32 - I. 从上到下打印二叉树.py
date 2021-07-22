'''
剑指 Offer 32 - I. 从上到下打印二叉树
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
 

提示：

节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 用队列来实现广度优先搜索
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        # 如果是空树，直接返回空列表
        if root==None: return []
        # 广度优先搜索，层序遍历，用队列实现
        queue = [root]
        result = []

        while queue!=[]: # 当队列不为空时
            for i in range(len(queue)):
                node = queue.pop(0) # 队列第一个元素弹出
                result.append(node.val) # 将该元素的值加入到result列表中
                if node.left!=None: # 往左边走，更新队列
                    queue.append(node.left)
                if node.right!=None: # 往右边走，更新队列
                    queue.append(node.right)

        return result