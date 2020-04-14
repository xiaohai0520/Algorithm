# 博弈问题

博弈问题一般都是两个人玩某种游戏，然后会获胜的那一方。这类问题往往是利用动态规划的原理，我们从一个状态转移到另外一个状态。最后得到的状态就是结果。
说起来很简单，让我们来详细的看一下博弈问题吧。

## 1.总体概述

**场景**：硬币问题，石子问题等。

**难点**：转移方程，先后手定义。

## 2.细节讲解
什么事**博弈问题**？博弈问题就是一个游戏，两个人玩，两个人轮流玩，玩的时候两个人都要遵守一个规则，最后告诉我他们谁先玩完。

通俗点讲就是两个玩家轮流游戏，每个人都基于局面有一个可以操作的集合（一般一致），达到某个条件游戏结束，问是否必胜或者某位玩家的最大收益。

我们假定两个玩家都是聪明的，总是会选择自己的最优解。

那怎么能将博弈游戏转换为动态规划的模板呢？

游戏的局面： 动态规划中的**状态**。

每个玩家的决策：动态规划的**转移方程**。

游戏的终止： 动态规划的**初始化**。

先手和后手其实是相对考虑的。当一个人是先手的时候，他的结果其实是取决于如果上一步他是后手的结果。这个地方可能不太好理解，我们用一个简单的例子来进行理解。

## 3.一个小栗子
取石子游戏，我们有一排石子，然后两个玩家轮流取石子，每次从右侧开始取，可以取一个或者两个，谁能取到最后一个石子就是赢家。

我们先来看一下简答的部分，游戏的终止，当玩家取到最后一个石子的时候终止。

**if n == 1**

当只有1个石头的时候，那一定是先手的赢。

**if n == 2**

当只有2个石头的时候，那一定也是先手的赢。

因为先手可以取一个或者两个。说明当 `n == 1 or n == 2`时，总是先手赢。

**if n == 3**

那么当石头有3个的时候呢？ 我们用A和B来进行说明，假设A是先手，A先拿：

如果A拿了1个，那个还剩2个石头，该B选择拿石头了，那么此时我们忘记A，把B当成此刻的先手，我们已经知道，当`n == 2`时，先手总是回赢，那么B就会赢，所以A会输。

如果A拿了2个，那个还剩1个石头，该B选择拿石头了，那么此时我们再次忘记A，把B当成此刻的先手，我们已经知道，当`n == 1`时，先手总是回赢，那么B就会赢，所以A会输。

所以当 `n == 3` 时，无论A(先手)怎么拿，都会输掉。

**if n == 4**

我们再往下看一步，假设现在有4个石头，还是A先先手，A先拿：

如果A拿了1个，那个还剩3个石头，该B选择拿石头了，那么此时我们忘记A，把B当成此刻的先手，我们已经知道，当`n == 3`时，先手总是回输，那么B就会输，所以A会赢。

如果A拿了2个，那个还剩2个石头，该B选择拿石头了，那么此时我们再次忘记A，把B当成此刻的先手，我们已经知道，当`n == 2`时，先手总是回赢，那么B就会赢，所以A会输。

那么我们现在知道了，A先手拿1个会赢，拿2个会输，那聪明的A一定会拿1的，对吧。

所以当 `n == 4` 时，先手（A）会赢。

此时我们是否已经看出一些门道了，先手能不能赢完全取决于下一时刻和下两时刻的状态。先手总是会拿对他有利的那一种情况，如果拿1个和2个，对输赢没有影响，那先手可以随便拿。
如果拿1个或者拿2个才能赢，先手一定会拿会赢的那种情况。

我们的转移方程可以写成：`dp[i] = !dp[i-1] or !dp[i-2]` 也可以写成 `dp[i] = !(dp[i-1] and dp[i-2])`

这里dp的每一个状态记录的是先手会不会赢，如果会赢，记成`True`，否则记成`False`。

理解这个转换方式就是，假设A是先手，A拿了一次，然后变成B拿，这个时候变成了B是先手，B也想赢，那B也会选择能赢的那一种情况，只有B的两种情况都会输的情况下，A才能赢。

所以我们可以写出这个问题的代码：
```
def canWin(n):
    if n <= 2:
        return True
    dp = [True] * n
    for i in range(2,n):
        dp[i] = not (dp[i-1) and dp[i-2])
    return dp[-1]
```

## 4.总结
这种博弈问题的关键是要找到dp定义的状态，然后通过每次选手都会进行最优选择来确定转移方程，最后可以轻易的解决博弈问题。

