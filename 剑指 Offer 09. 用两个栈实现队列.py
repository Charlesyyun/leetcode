'''
剑指 Offer 09. 用两个栈实现队列
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class CQueue:

    def __init__(self):
        self.li = []
        self.result = [None]
        #print('初始化后的队列为：{},结果为：{}'.format(self.li,self.result))

    def appendTail(self, value: int) -> None:
        self.li.append(value)
        self.result.append(None)
        #print('appendTail后的队列为：{},结果为：{}'.format(self.li,self.result))
        return self.result[-1]

    def deleteHead(self) -> int:
        if len(self.li)==0:
            self.result.append(-1)
            #print('当前队列为空，deleteHead后的队列为：{},结果为：{}'.format(self.li,self.result))
        else:
            self.result.append(self.li[0])
            self.li.remove(self.li[0])
            #print('deleteHead后的队列为：{},结果为：{}'.format(self.li,self.result))
        return self.result[-1]



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()