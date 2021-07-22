'''
剑指 Offer 33. 二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
 

提示：

数组长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 翻转后序遍历列表，顺序变成：根->右->左。根据右子树全都大于根来找出右子树。剩下的左子树元素逐个和根比较，出现大于根的元素就报错。然后递归各个子树。
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        # 二叉搜索树特性：左<根<右，后序遍历顺序是：左->右->根
        # 后序遍历的倒序是：根->右->左
        postorder.reverse()
        # 第一个是根节点，之后的一段全部大于根节点的是右子树，最后一段全部小于根节点的是左子树

        def checktree(postorder):
            root = 0 # 根节点索引
            if len(postorder)<=1: return True # 当待检查列表长度小于等于1时，返回True
            # 找出右子树
            for i in range(root+1,len(postorder)):
                if postorder[i] <= postorder[root]: # 发现不满足右子树条件就跳出循环
                    break
            postorder_left = postorder[root+1:i]
            # 查看剩下的左子树是否都小于根节点，若否，则返回False
            for j in range(i+1,len(postorder)):
                if postorder[j] >= postorder[root]:
                    return False
            postorder_right = postorder[i:]
            return checktree(postorder_left) and checktree(postorder_right)
        return checktree(postorder)