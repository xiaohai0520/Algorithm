## 301. Remove Invalid Parentheses

### 题目分析
给定一个由括号组成的字符串，也可能包含其他字符，然后我们需要删除一些括号，使字符串变得valid。

返回的结果是去掉最少括号后的所有可能的组合。


### 解法

先说判断一个string是不是合法的方法，我们按顺序去检查左括号和右括号，用left和right去计数，如果是左括号，那么left+1, 如果是右括号，此时left的值大于0的话，那left-1，否则right+1。

最后得出的left和right就是多出的左右括号，原则上我们只要删除这些多出的括号就可以得到合法的字符串了。


1.DFS

我们每次删去一个左括号或者右括号，那么就相应的在left和right上减一，直到left和right为0，这个时候在检查下是否是合法的。

为了避免重复，如果遇到连续的同一种括号，只删除第一个就好了。

2.BFS

我们从删除一个某种括号开始，然后逐层的检查所有的结果，看是否有至少一个是合法的，如果有则返回。




### 代码

DFS
```
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        count = self.getLeftRightCount(s)
        self.dfs(s, 0, count[0], count[1], result)
        return result
    def getLeftRightCount(self, s):
        count = [0] * 2
        for ch in s:
            if ch == "(":
                count[0] += 1
            elif ch == ")":
                if count[0] > 0:
                    count[0] -= 1
                else:
                    count[1] += 1
        return count
    def dfs(self, s, start, leftCount, rightCount, result):
        if leftCount == 0 and rightCount == 0 and self.isStringValid(s):
            result.append(s)
            return
        for i in range(start, len(s)):
            if i > start and s[i] == s[i - 1]:
                continue
            if rightCount > 0 and s[i] == ")":
                self.dfs(s[0:i] + s[i+1:], i, leftCount, rightCount - 1, result)    
            if leftCount > 0 and s[i] == "(":
                self.dfs(s[0:i] + s[i+1:], i, leftCount - 1, rightCount, result)
            
    def isStringValid(self, s):
        count = self.getLeftRightCount(s)
        return count[0] == 0 and count[1] == 0
```


BFS
```
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isval(s):
            res = 0
            for i in range(len(s)):
                if s[i] == '(':
                    res += 1
                elif s[i] == ')':
                    res -= 1
                if res < 0:
                    return False
            return res == 0
        
        level = {s}
        while 1:
            res = list(filter(isval,level))
            if res:
                return res
            level = {s[:i]+s[i+1:] for s in level for i in range(len(s))}
```
