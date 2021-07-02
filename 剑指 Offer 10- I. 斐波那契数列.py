'''
剑指 Offer 10- I. 斐波那契数列
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5
 

提示：

0 <= n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 动态规划数组的迭代解法
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            b, a = 1, 0 # 两个针指向数列的前两个位置(0,1,1,2,3,5,...)
            for i in range(n): # 遍历直至n为止，更新a和b所指的数
                b, a = a+b, b
            # 遍历到最后一个时候，a刚好就是f(n)对应的值;
            # i = 0时候，a = 1, b = 1;
            # i = 1时候，a = 1, b = 2;
            # i = 2时候，a = 2, b = 3;
            # i = 3时候，a = 3, b = 5;
            # 遍历终点是i=n-1时候，a = f(n), b = f(n+1)
            return a % 1000000007

# 基于缓存的递归解法
class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def recur(n):
            if n in cache:
                return cache[n]
            elif n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                cache[n] = recur(n-1) + recur(n-2)
            return cache[n]
        return recur(n)%1000000007