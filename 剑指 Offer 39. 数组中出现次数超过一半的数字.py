'''
剑指 Offer 39. 数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

 

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
 

限制：

1 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 方法一、取巧法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 需要的数字出现次数多于一半 那么排序后必定在中间
        return sorted(nums)[int(len(nums)/2)]

# 方法二、利用字典记录次数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cache = {}
        for i in range(len(nums)):
            if nums[i] not in cache:
                cache[nums[i]] = 1
            else:
                cache[nums[i]] += 1
            if cache[nums[i]]>=len(nums)/2:
                return nums[i]
        return None