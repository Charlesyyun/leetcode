'''
剑指 Offer 29. 顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix) # 行数
        if m == 0: return matrix
        n = len(matrix[0]) # 列数
        if n == 0: return matrix

        result = []
        x, y = 0, 0 # 初始化坐标

        for i in range(m*n):
            result.append(matrix[x][y]) # 加进结果列表
            matrix[x][y] = None # 走过的地方标记为None

            # 不可以走的地方：越界或者已经走过
            if y+1 < n and matrix[x][y+1]!=None and (y-1 < 0 or matrix[x][y-1]==None) and (x-1 <0 or matrix[x-1][y]==None): # 如果左和上被封，且可以往右走，那么就往右走
                y += 1
            elif x + 1 < m and matrix[x+1][y]!=None and (y+1 >= n or matrix[x][y+1]==None) and (x-1 <0 or matrix[x-1][y]==None): # 如果右和上被封，且可以往下走，那么就往下走
                x += 1
            elif y-1 >= 0 and matrix[x][y-1]!=None and (y+1 >= n or matrix[x][y+1]==None) and (x+1 >= m or matrix[x+1][y]==None): # 如果右和下被封，且可以往左走，那么就往左走
                y -= 1
            elif x-1 >= 0 and matrix[x-1][y]!=None and (y-1 < 0 or matrix[x][y-1]==None) and (x+1 >= m or matrix[x+1][y]==None): # 如果左和下被封，且可以往上走，那么就往上走
                x -= 1
            else:
                return result # 右下左上都没路的话，说明走完了，返回结果