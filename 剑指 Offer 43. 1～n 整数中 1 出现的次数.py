'''
剑指 Offer 43. 1～n 整数中 1 出现的次数
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

 

示例 1：

输入：n = 12
输出：5
示例 2：

输入：n = 13
输出：6
 

限制：

1 <= n < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def countDigitOne(self, n: int) -> int:
        # 思路：生活中的密码锁，固定一个位置为1，拨动其他位置，有多少可能性？
        # 把n看成字符串，从个位开始，固定每一位为1，计算其他位置的可能性，即可求出该位上1出现的次数
        # 初始化cur指向当前位，low表示地位，high表示高位
        low = 0
        cur = n % 10 # 初始化个位数字
        high = n //10 # 初始化为百位
        digit = 1 # 指示位数的因子，初始化为个位
        result = 0 # 累加：统计固定每个位置为1后，其他位置的可能性
        print('0.low: {}, cur:{}, high:{}, digit:{}, result: {}'.format(low,cur,high,digit,result))
        while low!=n: # 走到最后low就变成了n
            # 固定cur所在的digit位为1，统计其它位置的可能次数
            print('1.low: {}, cur:{}, high:{}, digit:{}, result: {}'.format(low,cur,high,digit,result))
            if cur == 0:
                result += high*digit
                print('2.low: {}, cur:{}, high:{}, digit:{}, result: {}'.format(low,cur,high,digit,result))
            elif cur == 1:
                result += high*digit+low+1
                print('3.low: {}, cur:{}, high:{}, digit:{}, result: {}'.format(low,cur,high,digit,result))
            else:
                result += (high+1)*digit
                print('4.low: {}, cur:{}, high:{}, digit:{}, result: {}'.format(low,cur,high,digit,result))
            low += cur*digit # low往左走，更新为cur的数字乘上位数
            cur = high%10 # cur往左走，更新为high的最后一位
            high = high//10 # high往左走
            digit *= 10 # 更新cur的位数
            print('5.low: {}, cur:{}, high:{}, digit:{}, result: {}'.format(low,cur,high,digit,result))
        return result