'''
剑指 Offer 36. 二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

 

为了让您更好地理解问题，以下面的二叉搜索树为例：

 



 

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。

 



 

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return None
        if root.left==None and root.right==None:
            root.left = root
            root.right = root
            return root
        # 二叉搜索树的中序遍历？左->中->右
        result = []
        def dfs(root,result):
            if not root: return
            dfs(root.left,result)
            result.append(root)
            dfs(root.right,result)

        dfs(root,result)

        if len(result)==2:
            result[0].left = result[1]
            result[0].right = result[1]
            result[1].left = result[0]
            result[1].right = result[0]
            head = result[0]
            return head
        result[0].left = result[-1]
        result[0].right = result[1]
        result[-1].left = result[-2]
        result[-1].right = result[0]
        for i in range(1,len(result)-1):
            result[i].left=result[i-1]
            result[i].right=result[i+1]
        head = result[0]
        return head