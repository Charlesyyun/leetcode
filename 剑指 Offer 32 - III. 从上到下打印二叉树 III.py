'''
剑指 Offer 32 - III. 从上到下打印二叉树 III
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

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
  [20,9],
  [15,7]
]
 

提示：

节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 添加奇偶数层数判断，偶数层就逆序输出
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 尝试在层序遍历的基础上修改
        if root==None: return []
        # 初始化queue和result
        queue = [root]
        result = []
        n = 1 # 层数编号，从第一层开始
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
            if n % 2 == 0: # 如果是偶数层，逆序输出level数组
                level.reverse()
            result.append(level)
            n += 1
        return result