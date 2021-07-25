'''
剑指 Offer 35. 复杂链表的复制
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

 

示例 1：



输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：



输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：



输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
 

提示：

-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 枚举解决空链表以及单个节点链表的特殊情况
        if head == None: return None
        if head.next == None:
            result = Node(head.val)
            result.next = None
            if head.random == None:
                result.random = None
            else:
                result.random = result
            return result

        # 初始化两个列表来存原链表的每一个节点和random节点
        li_node = []
        random_node = []

        # 在li_node和random_node记录每一个节点
        while head != None:
            li_node.append(head)
            random_node.append(head.random)
            head = head.next

        # 找到random_node在li_node中的序号(索引)
        random_node_index = []
        for i in range(len(random_node)):
            if random_node[i] == None:
                random_node_index.append(None)
            for j in range(len(li_node)):
                if random_node[i] == li_node[j]:
                    random_node_index.append(j)

        # 根据li_node重建新的链表
        result = Node(li_node[0].val)
        result.next = Node(li_node[1].val)
        temp = result.next
        match = {0: result, 1: result.next}  # 用字典存下新建的节点及其索引
        for k in range(2, len(li_node)):
            temp.next = Node(li_node[k].val)
            match[k] = temp.next
            temp = temp.next

        # 根据random_node_index为新的链表添加random属性
        for l in range(len(li_node)):
            if random_node_index[l] == None:
                match[l].random = None
            else:
                match[l].random = match[random_node_index[l]]
        return result
