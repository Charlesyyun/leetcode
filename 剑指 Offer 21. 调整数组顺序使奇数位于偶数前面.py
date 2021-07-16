'''
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
 

提示：

0 <= nums.length <= 50000
1 <= nums[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 方法一、暴力遍历
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        def iseven(x):
            if x == 0: return True
            elif x == 1: return False
            elif x%2 == 0: return True
            else: return False
        result = []
        for i in nums:
            if iseven(i)==True:
                result.append(i)
            else:
                result.insert(0,i)
        return result

# 方法二、首尾指针
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        start_index = 0
        end_index = len(nums)-1
        while start_index < end_index:
            if nums[start_index]==1 or nums[start_index]%2==1: # 如果左边指针指向奇数，则不做调整，直接指向下一个
                start_index += 1
            else: #  如果左边指针指向偶数，那么看看右边指针指向什么
                if nums[end_index]==1 or nums[end_index]%2==1: # 如果右边指针指向奇数，那么和左边指向偶数的指针调换值
                    nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
                    # 交换完成后，左指针继续往右走，右指针继续往左走
                    start_index += 1
                    end_index -= 1
                else: # 如果右边指针指向偶数，那么右边指针往左走
                    end_index -= 1
        return nums
