'''
剑指 Offer 16. 数值的整数次方
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。

 

示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：

输入：x = 2.10000, n = 3
输出：9.26100
示例 3：

输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
 

提示：

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1  # 如果n=0,直接返回1
        elif n == 1:
            return x  # 如果n=1，直接返回x
        elif n > 1:  # 如果n>1
            if n % 2 == 0: return self.myPow(x * x, n / 2)  # 如果指数是偶数，可以写成pow(x*x,n/2)来成半减少指数部分
            return x * self.myPow(x, n - 1)  # 如果指数不是偶数，那就递归把指数减1
        elif n < 0:  # 如果指数是负数
            return 1 / self.myPow(x, -n)
