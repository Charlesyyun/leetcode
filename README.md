# leetcode
刷题的记录
先刷剑指offer吧~

**深度优先搜索心得：**
1. 创建二维数组（矩阵），方便改写每次访问过的位置（比如改成0或者1或者True等等），防止后续重复计数；
2. 在主函数中写出问题的最初起点，调用dfs函数进行递归；
3. 写dfs函数：
（1）先写递归出口（例如：越过边界，矩阵位置已被访问过，不满足题目给定约束条件等等）return False或者0；
（2）然后如果没有满足递归出口条件，则改写当前访问到的矩阵位置的值，防止后续被再次访问；
（3）再写从母问题到子问题的递归式，return True或者需要递归计算的内容；

**动态规划心得：**

*递归和动态规划都是将原问题拆成多个子问题然后求解，他们之间最本质的区别是，动态规划保存了子问题的解，避免重复计算。*

1. 常用于给定约束条件下的优化问题；
2. 找到母问题和子问题的关系；
3. 任何动态规划都涉及网络；
4. 单元格的值就是要优化的目标值，每一个单元格就是一个子问题；

**二叉树：**
1. 三种遍历：前序（根->左->右），中序（左->根->右），后序（左->右->根）。可以看出，前中后指的是根所在的位置。
2. 常规遍历的算法通常有两种：

 (1)递归解法（dfs)：前中后遍历的话调换一下result.append(root.val)的位置即可；
 ![Load Failed](https://pic.leetcode-cn.com/c00cf3325eaf0037d35f15c811d747c22980f7df5b82ea90958199ef5edbb321.png)
 ```
      def dfs(root,result):
        if root==None: return
        result.append(root.val)
        dfs(root.left)
        dfs(root.right)
 ```
 (2)用栈来迭代：我们使用栈来进行迭代，过程如下：
    初始化栈，并将根节点入栈；
    当栈不为空时：
    弹出栈顶元素 node，并将值添加到结果中；
    如果 node 的右子树非空，将右子树入栈；
    如果 node 的左子树非空，将左子树入栈；
    由于栈是“先进后出”的顺序，所以入栈时先将右子树入栈，这样使得前序遍历结果为 “根->左->右”的顺序。
    ![Load Failed](https://pic.leetcode-cn.com/1603759550-TUinjp-14.png)
 ```
      def preorderTraversal(root):
        if root==None: return []
        stack = [root]
        result = []
        while stack!=[]:
          node = stack.pop()
          result.append(node.val)
          if node.right!=None:
            stack.append(node.right)
          if node.left!=None:
            stack.append(node.left)
        return result
  ```
        
3. 非常规的奇葩遍历，层序遍历：用队列来迭代（先进先出）
![Load Failed](https://pic.leetcode-cn.com/68bd2b9b62ec200ad68843565e06fcb238ee7e83f7385deb825920b9889175df.png)
```
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None: return []
        # 初始化queue和result
        queue = [root]
        result = []
        # 对queue进行循环,非空就循环
        while queue!=[]:
            level = [] # 初始化该层的列表
            for i in range(len(queue)):
                node = queue.pop(0) # 先进先出
                level.append(node.val) # 往该层列表append队列中出来的值
                if node.left != None: # 往左子树更新队列
                    queue.append(node.left)
                if node.right != None: # 往右子树更新队列
                    queue.append(node.right)
            result.append(level)
        return result
```
4. 二叉树的路径遍历，好像必须用字符串的形式记录，否则会输出整个遍历的二叉树
```
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # 先写一个函数来记录所有的路径
        path = '' # 还在走的每一个路径
        paths = [] # 已经走到叶子节点的路径
        def construct_path(root,path):
            if root: # 如果该节点不为None，加入到path
                path += str(root.val)
                if not root.left and not root.right: # 如果已经走到了叶子节点
                    paths.append(path) # 记录走完毕的该路径
                else:
                    # 如果还没走到叶子节点，继续递归
                    path += '->'
                    construct_path(root.left,path)
                    construct_path(root.right,path)

        construct_path(root,path) # 调用写好的路径记录函数，将所有路径存入paths列表
        return paths
```

5. 回溯法（专门解决N层嵌套循环写不出来的问题）：暴力求解排列组合问题、切割问题、子集问题、棋盘问题。可以抽象成N叉树形结构。
```
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
                    used[i] = 1
                    path.append(s[i])
                    backtracking(s,path,used)
                    # 回溯复原
                    path.pop()
                    used[i] = 0
        backtracking(s,path,used)
        result = list(set(result))
        return result
```
