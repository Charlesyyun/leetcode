'''
剑指 Offer 44. 数字序列中某一位的数字
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

 

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0
 

限制：

0 <= n < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def findNthDigit(self, n: int) -> int:
        # 先找出N对应数字的位数
        # 数x的位数d= 1,2,3,4...
        # 数x = 0~9, 10~99, 100~999, 1000~9999...
        # 位置n = 0~9, 10~189, 190~2889, 2890~38889...
        if n < 10: return n
        # 第一步：位置n有几位？
        digit_n = len(str(n))
        # 第二步：位置n可能落在哪个范围？例如，三位数的n可能落在10~189，也可能落在190~2889，那么先把189这个参考值表示出来
        reference = str(digit_n-2) + '8' * (digit_n-2) + '9' # 把参考值189表示出来
        reference = int(reference)

        left = int(str(digit_n-3) + '8' * (digit_n-3) + '9')+1 # 把左边的值10表示出来
        right = int(str(digit_n-1) + '8' * (digit_n-1) + '9') # 把右边的值2889表示出来
        # 第三步：根据位置n的范围，确定数x的范围
        if n > reference: # n落在右边，即190~2889
            range_n = [reference+1,right]
            range_x = [pow(10,len(str(range_n[0]))-1),pow(10,len(str(range_n[0])))-1]
            digit_x = len(str(range_x[0])) # 确定数x的位数
        else: # n落在左边，即10~189
            range_n = [left, reference]
            range_x = [pow(10,len(str(range_n[0]))-1),pow(10,len(str(range_n[0])))-1]
            digit_x = len(str(range_x[0])) # 确定数x的位数

        # 第四步：确定在n的范围内用了几个格子
        pos_used = n - range_n[0] + 1

        # 第五步：求出在n的范围内可以存几个数（除去x之外）
        number_saved = (n-range_n[0]+1)//digit_x

        # 第六步：求出当前数
        if (n-range_n[0]+1)%digit_x == 0: # 刚好除尽
            x = number_saved + range_x[0] - 1
        else: # 除不尽，多余的格子装不下当前数X的所有数字
            x = number_saved + range_x[0]

        # 第七步：求出剩余几个格子可以存当前数
        remain = (n-range_n[0]+1) % digit_x

        # 第八步：求出当前数的最后一个格子存的什么数字
        result = str(x)[remain-1]

        return int(result)
