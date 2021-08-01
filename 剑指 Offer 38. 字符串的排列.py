'''
剑指 Offer 38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 

限制：

1 <= s 的长度 <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 回溯法经典例题
class Solution:
    def permutation(self, s: str) -> List[str]:
        result = [] # 存放最终结果
        path = [] # 存放每条路径
        used = [0] * len(s) # 标记对应元素是否已经使用过
        def backtracking(s,path,used):
            # 终止条件
            if len(path)==len(s):
                result.append(''.join(path))
                return
            for i in range(len(s)):
                if used[i]==0: # 第i个元素没被用过
                    if i>0 and s[i] == s[i-1] and not used[i-1]: # 去重，如果s[i]和s[i-1]一样且s[i-1]没用过
                        continue
                    used[i] = 1
                    path.append(s[i])
                    backtracking(s,path,used)
                    # 回溯复原
                    path.pop()
                    used[i] = 0
        backtracking(sorted(s),path,used)
        return result