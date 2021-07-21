'''
剑指 Offer 30. 包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 

提示：

各函数的调用总次数不超过 20000 次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[] # 初始化栈
        self.minimum=[] # 初始化每次更新后的最小值列表，最小值在最后append


    def push(self, x: int) -> None:
        self.stack.append(x) # 压入栈
        if self.minimum==[] or self.minimum[-1]>=x: # 如果最小值列表是空的，或者最小值列表的最后一位元素大于等于当前压入的元素，那么在最小值列表最后append该元素
            self.minimum.append(x)

    def pop(self) -> None:
        if self.stack[-1]==self.minimum[-1]: # 如果弹出的栈顶元素等于最小值列表的最后一个元素（即当前最小值），那么弹出的同时也删去最小值列表的最后一个元素
            del(self.minimum[-1])
        return self.stack.pop()

    def top(self) -> int:
        if len(self.stack)>0: # 如果栈非空，那么返回栈顶元素
            return self.stack[-1]
        else:
            return None # 如果是空栈，返回None

    def min(self) -> int:
        return self.minimum[-1] # 直接返回最小值列表的最后一个元素即可

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()