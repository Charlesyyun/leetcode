'''
剑指 Offer 32 - II. 从上到下打印二叉树 II
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
 

提示：

节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 还是队列实现的层序遍历，但是要创建一个层的列表来存值，从而方便区分每一层的值
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 跟上一题一样都是层序遍历，不过这次要明确分层
        if root==None: return []
        # 初始化queue和result
        queue = [root]
        result = []
        # 对queue进行循环,非空就循环
        while queue!=[]:
            level = [] # 初始化该层的列表
            for i in range(len(queue)):
                node = queue.pop(0) # 先进先出
                level.append(node.val) # 往该层列表append队列中出来的值
                if node.left != None: # 往左子树更新队列
                    queue.append(node.left)
                if node.right != None: # 往右子树更新队列
                    queue.append(node.right)
            result.append(level)
        return result