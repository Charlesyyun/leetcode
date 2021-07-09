'''
剑指 Offer 14- I. 剪绳子
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示：

2 <= n <= 58

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 数学推理法
class Solution:
    def cuttingRope(self, n: int) -> int:
        # 对于长度小于等于3的绳子，直接枚举返回
        if n == 2: product = 1
        elif n == 3: product = 2
        else:
            # 对于总长度大于3的绳子，可以证明分成每段都是3的情况下可以达到最大（要求n/m余数不是1）
            left = n % 3 # 试着把每段长度划分为3，看看余数是多少
            if left == 0: # 如果余数是0的话，那么每段长度为3，段数等于n/3
                product = pow(3,n/3)
            elif left == 2: # 如果余数是2的话，那么有1段长度为2，(n-2)/3段长度为3
                product = pow(3,(n-2)/3)*2
            elif left == 1: # 如果余数为1的话，那么取出一段长度为3的绳子和1合并再均分，最终有2段2米的绳子，(n-4)/3段3米的绳子
                product = pow(3,(n-4)/3)*2*2
        return int(product)

# 动态规划递归法
class Solution:
    def cuttingRope(self, n: int) -> int:
        # 动态规划：长度为i的绳子可以分成长度为j和长度为i-j的子绳，递归求其最优乘积
        # 创建dp数组记录长度i的最优乘积
        dp = [0 for _ in range(n+1)]
        # 如果长度为2,3，直接枚举返回
        if n <= 3: return n-1

        # 递归基线：长度为2,3的特殊例子先给定值,这些都是分割以后乘积小于本身的，直接定值为本身
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        # 循环求解子问题
        for i in range(4,n+1):
            for j in range(1,i//2+1):
                dp[i] = max(dp[i],dp[j]*dp[i-j])
                # print('i={},j={},dp={}'.format(i,j,dp))
        return dp[n]