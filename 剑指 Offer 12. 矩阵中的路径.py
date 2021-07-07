'''
剑指 Offer 12. 矩阵中的路径
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。



 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
 

提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
board 和 word 仅由大小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                w = 0
                if dfs(board, word, i, j, w):
                    return True
        return False

def dfs(board, word, i, j, w):
    # 边界溢出or不相等的情况
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[w]:
        return False
    # 如果word判断完了：
    if w == len(word) - 1:
        return True
    # 记录并修改当前位置的值，防止被后续访问
    tmp = board[i][j]
    board[i][j] = "."
    # 寻找上下左右四个方向
    res = dfs(board, word, i-1, j, w+1) or dfs(board, word, i+1, j, w+1) or dfs(board, word, i, j-1, w+1) or dfs(board, word, i, j+1, w+1)
    board[i][j] = tmp
    return res