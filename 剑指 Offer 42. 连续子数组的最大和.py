'''
剑指 Offer 42. 连续子数组的最大和
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

 

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 

提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划，网格长度等于nums，网格内容是待优化内容dp[i]：以该点结尾的子数组的最大和
        dp = nums.copy()
        for i in range(1,len(nums)):
            if dp[i-1]<=0: # 如果dp[i-1]小于等于0，说明dp[i-1]对dp[i]产生负贡献
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i] # 如果dp[i-1]大于0，产生正贡献，那么dp[i] = dp[i-1]+nums[i]
        return max(dp)