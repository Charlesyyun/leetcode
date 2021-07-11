'''
剑指 Offer 18. 删除链表的节点
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

说明：

题目保证链表中节点的值互不相同
若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法一、转换成列表来做
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 先想办法把输入的链表转换为列表，然后在列表里删去指定值
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        temp.remove(val)
        # temp长度小于等于1时：
        if len(temp)==0: return ListNode(None)
        elif len(temp)==1: return ListNode(temp[0])
        # temp的长度大于等于2时
        temp_head = ListNode(temp[0])
        t = ListNode(temp[1])
        temp_head.next = t
        for i in range(2,len(temp)):
            t.next = ListNode(temp[i])
            t = t.next
        return temp_head

# 方法二、直接更改链表的指向
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 枚举要删除的点在头两个的情况
        if head.val == val: return head.next
        if head.next.val == val:
            head.next=head.next.next
            return head

        # 如果要删除的点在第三个及之后，循环检查是否有节点等于要删除的值，如果是的话，就更改该节点的上一个点的指针指向该节点的下一个点
        t = head.next # 令t指向原链表的下一个节点
        while t: # 当t不是None的时候进行循环
            if t.next==None: return head # 如果t的下一个节点是None，那么说明已经走完了，直接返回head
            if t.next.val == val: # 如果t节点的下一个节点的值是要删除的值
                t.next = t.next.next # 跳过待删除值，直接将t.next指向t.next.next
            t = t.next # 将t赋值为t的下一个节点，进行下一次循环
        return head # 循环完成以后，返回head值