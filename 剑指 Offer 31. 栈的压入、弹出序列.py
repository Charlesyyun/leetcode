'''
剑指 Offer 31. 栈的压入、弹出序列
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

 

示例 1：

输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
示例 2：

输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。
 

提示：

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed 是 popped 的排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 方法一、辅助栈模拟，判断最终是不是空栈就行了
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num) # num 入栈
            while stack and stack[-1] == popped[i]: # 循环判断与出栈
                stack.pop()
                i += 1
        return not stack

# 方法二、模拟整个过程，比较模拟的弹出序列和输入的弹出序列
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 如果两个序列不等长，直接返回False
        if len(pushed)!=len(popped): return False
        # 正常来讲应该就是压入序列的逆序，但是例子中先4后5是怎么发生的呢？
        # 其实就是在压入过程中有了弹出操作，导致了先4后5的情况；

        # 预先存下输入数据以便后续判断
        cache_pushed = pushed.copy()
        cache_popped = popped.copy()

        # 尝试模拟压入过程
        stack = []
        pop_simu = []

        while pushed!=[]: # pushed不为空时，进入循环
            if stack!=[] and popped!=[] and stack[-1]==popped[0]: # 首先，如果原栈顶元素和popped的首个元素相同，则可以弹出栈顶元素
                pop_simu.append(popped[0])
                del(stack[-1])
                del(popped[0])
            elif pushed[0]!=popped[0]: # 如果pushed的首元素和popped的首元素不同
                stack.append(pushed[0]) # 那么照常压入pushed的首元素到stack
                del(pushed[0]) # 同时删去pushed的首元素
            elif pushed[0]==popped[0]: # 如果pushed首元素和popped首元素相同
                pop_simu.append(popped[0]) # 将popped首元素加入到pop_simu来记录压入过程中弹出的元素
                del(pushed[0]) # 删去pushed的首元素
                del(popped[0]) # 删去popped的首元素
        print('pushed:{},popped:{},stack:{},pop_simu:{}'.format(pushed,popped,stack,pop_simu))

        # 模拟弹出过程
        for _ in range(len(stack)):
            if stack[-1]!=None:
                pop_simu.append(stack[-1])
                stack.pop()
        print('pushed:{},popped:{},stack:{},pop_simu:{}'.format(pushed,popped,stack,pop_simu))
        if pop_simu == cache_popped:
            return True
        else:
            return False