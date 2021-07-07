'''
剑指 Offer 11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 暴力破解
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        sorted_list = sorted(numbers)
        return sorted_list[0]

# 二分查找
# 寻找旋转数组的最小元素即为寻找右排序数组的首个元素 nums[x]，称 x 为 旋转点 。
# 排序数组的查找问题首先考虑使用 二分法 解决，其可将 遍历法 的 线性级别 时间复杂度降低至 对数级别 。
#
# 算法流程：
# 初始化： 声明 i, j双指针分别指向 nums数组左右两端；
# 循环二分： 设 m = (i + j) / 2m=(i+j)/2 为每次二分的中点（ "/" 代表向下取整除法，因此恒有 i \leq m < ji≤m<j ），可分为以下三种情况：
# 当 nums[m] > nums[j]nums[m]>nums[j] 时： mm 一定在 左排序数组 中，即旋转点 xx 一定在 [m + 1, j][m+1,j] 闭区间内，因此执行 i = m + 1i=m+1；
# 当 nums[m] < nums[j]nums[m]<nums[j] 时： mm 一定在 右排序数组 中，即旋转点 xx 一定在[i, m][i,m] 闭区间内，因此执行 j = mj=m；
# 当 nums[m] = nums[j]nums[m]=nums[j] 时： 无法判断 mm 在哪个排序数组中，即无法判断旋转点 xx 在 [i, m][i,m] 还是 [m + 1, j][m+1,j] 区间中。解决方案： 执行 j = j - 1j=j−1 缩小判断范围，分析见下文。
# 返回值： 当 i = ji=j 时跳出二分循环，并返回 旋转点的值 nums[i]nums[i] 即可。
#
# 作者：jyd
# 链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # 二分查找旋转点
        # 初始化指针i,j；分别指向首尾
        i,j = 0,len(numbers)-1

        while i < j:
            mid = (i+j)//2
            if numbers[mid] > numbers[j]:
                # 旋转点在区间[mid+1,j],把指针i指向mid的右边
                i = mid+1
            elif numbers[mid] < numbers[j]:
                # 旋转点在区间[i,mid],把指针j指向mid的左边
                j = mid
            else:
                #当numbers[mid] = numbers[j],无法判断旋转点在哪,减小j缩小范围继续循环
                j = j-1
        # 循环结束时，i==j，此时指向的就是旋转点
        return numbers[i]
