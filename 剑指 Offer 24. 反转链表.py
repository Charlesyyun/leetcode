'''
剑指 Offer 24. 反转链表
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 

限制：

0 <= 节点个数 <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 顺序遍历缓存节点，然后逆序复原
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 如果输入空链表，直接返回head
        if head == None: return head
        # 如果输入非空链表，则往下走
        cache={}
        cache[0] = head.val
        i = 1
        while head.next!=None:
            cache[i] = head.next.val
            head = head.next
            i += 1
        # 循环结束的时候i=链表长度值, head是原链表最后一个节点
        length = i
        # 如果length等于1
        if length==1: return head
        # 如果length等于2
        if length==2:
            head.next = ListNode(cache[0])
            return head
        # 如果length大于等于3
        result = ListNode(cache[length-1])
        result.next = ListNode(cache[length-2])
        temp = result.next
        j = length-3
        while j>=0:
            temp.next = ListNode(cache[j])
            temp = temp.next
            j -= 1
        return result