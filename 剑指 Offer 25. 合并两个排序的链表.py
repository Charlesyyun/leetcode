'''
剑指 Offer 25. 合并两个排序的链表
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        cache = []
        # 遍历缓存链表1
        if l1 != None:
            cache.append(l1.val)
            while l1.next != None:
                cache.append(l1.next.val)
                l1 = l1.next

        # 遍历缓存链表2
        if l2 != None:
            cache.append(l2.val)
            while l2.next != None:
                cache.append(l2.next.val)
                l2 = l2.next

        # 缓存列表排序
        cache = sorted(cache)
        # 如果缓存列表为空
        if cache == []: return l1
        # 如果缓存列表长度为1
        if len(cache) == 1: return ListNode(cache[0])
        # 如果缓存列表长度为2
        if len(cache) == 2:
            result = ListNode(cache[0])
            result.next = ListNode(cache[1])
            return result
        # 如果缓存列表长度大于等于3，循环把缓存列表转换为链表
        result = ListNode(cache[0])
        result.next = ListNode(cache[1])
        temp = result.next
        i = 2
        while i < len(cache):
            temp.next = ListNode(cache[i])
            temp = temp.next
            i += 1
        return result