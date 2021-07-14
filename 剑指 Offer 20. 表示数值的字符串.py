'''
剑指 Offer 20. 表示数值的字符串
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。

数值（按顺序）可以分成以下几个部分：

若干空格
一个 小数 或者 整数
（可选）一个 'e' 或 'E' ，后面跟着一个 整数
若干空格
小数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字
整数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
至少一位数字
部分数值列举如下：

["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
部分非数值列举如下：

["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]
 

示例 1：

输入：s = "0"
输出：true
示例 2：

输入：s = "e"
输出：false
示例 3：

输入：s = "."
输出：false
示例 4：

输入：s = "    .1  "
输出：true
 

提示：

1 <= s.length <= 20
s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 方法一、写正则表达式
class Solution:
    def isNumber(self, s: str) -> bool:
        # # 小数正则表达式
        # pattern_decimal1 = '[\+-]?[0-9]+\.'
        # pattern_decimal2 = '[\+-]?[0-9]+\.[0-9]+'
        # pattern_decimal3 = '[\+-]?\.[0-9]+'
        # # 整数正则表达式
        # pattern_integer = '[\+-]?[0-9]+'
        # # 数值正则表达式
        # pattern_number1 = '(\s)?'+ (pattern_decimal or pattern_integer) + '(\s)?'
        # pattern_number2 = '(\s)?'+ (pattern_decimal or pattern_integer) + 'e' + pattern_integer + '(\s)?'
        # pattern_number3 = '(\s)?'+ (pattern_decimal or pattern_integer) + 'E' + pattern_integer + '(\s)?'

        # 最终枚举
        pattern_d1n1 = '(\s)*[\+-]?[0-9]+\.(\s)*'
        pattern_d2n1 = '(\s)*[\+-]?[0-9]+\.[0-9]+(\s)*'
        pattern_d3n1 = '(\s)*[\+-]?\.[0-9]+(\s)*'
        pattern_in1 = '(\s)*[\+-]?[0-9]+(\s)*'

        pattern_d1n2 = '(\s)*[\+-]?[0-9]+\.e[\+-]?[0-9]+(\s)*'
        pattern_d2n2 = '(\s)*[\+-]?[0-9]+\.[0-9]+e[\+-]?[0-9]+(\s)*'
        pattern_d3n2 = '(\s)*[\+-]?\.[0-9]+e[\+-]?[0-9]+(\s)*'
        pattern_in2 = '(\s)*[\+-]?[0-9]+e[\+-]?[0-9]+(\s)*'

        pattern_d1n3 = '(\s)*[\+-]?[0-9]+\.E[\+-]?[0-9]+(\s)*'
        pattern_d2n3 = '(\s)*[\+-]?[0-9]+\.[0-9]+E[\+-]?[0-9]+(\s)*'
        pattern_d3n3 = '(\s)*[\+-]?\.[0-9]+E[\+-]?[0-9]+(\s)*'
        pattern_in3 = '(\s)*[\+-]?[0-9]+E[\+-]?[0-9]+(\s)*'

        # 匹配结果
        match_d1n1 = re.match(pattern_d1n1,s)
        match_d2n1 = re.match(pattern_d2n1,s)
        match_d3n1 = re.match(pattern_d3n1,s)
        match_in1 = re.match(pattern_in1,s)

        match_d1n2 = re.match(pattern_d1n2,s)
        match_d2n2 = re.match(pattern_d2n2,s)
        match_d3n2 = re.match(pattern_d3n2,s)
        match_in2 = re.match(pattern_in2,s)

        match_d1n3 = re.match(pattern_d1n3,s)
        match_d2n3 = re.match(pattern_d2n3,s)
        match_d3n3 = re.match(pattern_d3n3,s)
        match_in3 = re.match(pattern_in3,s)

        # 写成列表，方便遍历
        match_list = [match_d1n1,match_d2n1,match_d3n1,match_in1,match_d1n2,match_d2n2,match_d3n2,match_in2,match_d1n3,match_d2n3,match_d3n3,match_in3]

        # 遍历确认，若全部返回None，则匹配失败返回False；
        # 若某一项返回不是None，则继续看这一项匹配结果和输入字符串是否一样，若一样，可以返回True
        for i in match_list:
            if i != None:
                if i.group(0)==s:
                    return True
        return False
