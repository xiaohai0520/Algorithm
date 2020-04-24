# 回溯算法

写在最前面，第一次接触回溯算法还是在两年前，很清楚的记得是第四周的JAVA编程课的作业，找出迷宫中的路径。大家都在说用回溯算法，当时我的还是一脸懵逼，什么是
回溯算法，结果那次的作业就一塌糊涂。现在想想，回溯不过就是一种暴力解，让电脑去做所有的尝试，找到答案而已。


## 1.总体概述
**场景**：N皇后，迷宫，数独等。

## 2.回溯框架
```
res = []
def backtrack(path,list):
    if 满足条件：
        res.append(path)
        return
    for each in list：
        处理选择
        backtrack(newpath,newlist)
        撤销选择
```

## 3.回溯思想
对于回溯问题，我们可以想成其实是遍历一颗决策树。

我们每次保留当前的路径，然后从选择列表里再调出下一步，然后在路径中添加新的一步，当决策树到底层，没有可选的了，如果此时满足条件，说明该路径为一个解。

## 4.举个栗子
给定任意几个数，然后我们求这几个数的所有排列组合。

比方说给定数组`[1,2,3]`,然后找出所有的排列。

先固定第一位为 1，然后第二位可以是 2，那么第三位只能是 3；然后可以把第二位变成 3，第三位就只能是 2 了；然后就只能变化第一位，变成 2，然后再穷举后两位。

其实这个本质就是回溯算法，那怎么将这个问题套入我们的框架里呢？

然后我们来一步一步的看一下：

我们先建立一个存储所有结果的数组`res = []`和一个存储排列过程的数组`path = []`。

我们有了这两个数组之后，想一下，终止条件是什么，是我们往path中加入了所有的数字时就可以停止了，将这个path加入res中，即`len(path) = len(nums)`。

那我们应该怎么做backtrack呢？

每次往path中加一个没加过的数字,这个过程其实是处理选择。即`path.append(num)`。

然后我们进行backtrack。

撤销就是将这个新加入的数字删除，`path.pop()`。

**代码**：

```
path = []
res = []
nums = [1,2,3]
def backtrack(path,nums,res):
    if len(path) == len(nums):
        res.append(path)
        return
    for i in range(len(nums)):
        if nums[i] in path:
            continue
        path.append(nums[i])
        backtrack(path,nums,res)
        path.pop()
```

当然有比较简洁的方式，就是每次在nums中删去已经加入的数字，知道nums中没有数字了。
```
def backtrack(path,nums,res):
    if not nums:
        res.append(path)
        return
    for i in range(len(nums)):
        backtrack(path+[nums[i]],nums[:i]+nums[i+1:],res)
```
## 5.总结
回溯算法本质上遍历一颗多叉树的问题，关键就是在遍历的过程中药做一些操作，记录path。

在某些方面，回溯其实是动态规划的暴力解，而动态规划会记录每一步，省去了一些可能重复的子问题。当我们再回溯中加入备忘录，就变成了从上到下的动态规划。
