'''
剑指 Offer 13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        matrix = [[0 for i in range(n)] for j in range(m)]
        i = 0
        j = 0
        return dfs(i, j, k, m, n, matrix)


def sum_digits(i, j):
    return i % 10 + j % 10 + i // 10 + j // 10


def dfs(i, j, k, m, n, matrix):
    if i < 0 or i >= m or j < 0 or j >= n:
        # print('i,j越过边界：',i,j)
        return 0
    elif sum_digits(i, j) > k:
        # print('i,j数位和大于k：',i,j,k)
        return 0
    elif matrix[i][j] == True:
        # print("矩阵位置i,j已经被访问过",i,j)
        return 0

    matrix[i][j] = True
    # print('符合要求，记录(i,j,matrix):',i,j,matrix)
    return 1 + dfs(i - 1, j, k, m, n, matrix) + dfs(i + 1, j, k, m, n, matrix) + dfs(i, j - 1, k, m, n, matrix) + dfs(i,
                                                                                                                      j + 1,
                                                                                                                      k,
                                                                                                                      m,
                                                                                                                      n,
                                                                                                                      matrix)
