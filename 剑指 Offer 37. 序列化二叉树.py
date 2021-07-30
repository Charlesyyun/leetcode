'''
剑指 Offer 37. 序列化二叉树
请实现两个函数，分别用来序列化和反序列化二叉树。

你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

 

示例：


输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 应该是要层序遍历
        if not root: return '[]'
        result, queue = [], [root]
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node == None:
                    result.append(None)
                else:
                    result.append(node.val)
                    if not node.left:
                        queue.append(None)
                    if node.left:
                        queue.append(node.left)
                    if not node.right:
                        queue.append(None)
                    if node.right:
                        queue.append(node.right)
        # 把末尾的None去掉（例如4和5的子树为None）
        for j in range(len(result)):
            if result[len(result) - j - 1] == None and result[len(result) - j - 2] != None:
                del (result[len(result) - j - 1:])
                break

        return str(result).replace('None', 'null').replace(' ', '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]': return []
        # 把data转换成二叉树节点列表
        data = data.replace('null', 'None')
        data = data.replace('[', '')
        data = data.replace(']', '')
        data = data.split(',')
        for i in range(len(data)):
            if data[i] == 'None':
                data[i] = None
            else:
                data[i] = TreeNode(int(data[i]))

        # 把列表转换为二叉树，注意层序遍历列表中父节点与子节点的索引下标关系
        # 父亲~左孩子：i~2i+1, 父亲~右孩子：i~2i+2
        j = 0  # 为了解决二叉树不是完全二叉树的问题（例如：[5,2,3,null,null,2,4,3,1]），如果出现一个None，则给j+2，来调整父与子的索引关系
        for i in range(len(data)):
            if 2 * i + 1 - j < len(data) and data[i] != None:
                data[i].left = data[2 * i + 1 - j]
            if 2 * i + 2 - j < len(data) and data[i] != None:
                data[i].right = data[2 * i + 2 - j]
            if data[i] == None:
                j += 2
        return data[0]


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))