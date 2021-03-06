'''
剑指 Offer 10- II. 青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1
提示：

0 <= n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def numWays(self, n: int) -> int:
        # 通过归纳容易发现输出的y是个斐波那契数列
        # n = 0,1,2,3,4,5,...
        # y = 1,1,2,3,5,8,...
        # 递归方程：f(n) = f(n-2)+f(n-1)
        cache = {}
        if n == 0: return 1
        # 初始化两个指针指向前一个数和后一个数
        b, a = 1, 1
        for i in range(n):
            b, a = a+b, b
            cache[i+1] = a
        return cache[n]%1000000007
