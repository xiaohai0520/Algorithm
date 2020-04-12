# 二分查找详解

写在最前面，当年老子学习二分法的时候，感觉这玩意就是so easy嘛，无论是quiz还是final中的二分法都没办法从我这里扣分。

这种蜜汁自信一直延续到我开始刷了力扣，二分法真的是噩梦般的存在，再也没有人让我去找特定的目标值了，什么第一个大于，最后一个小于，左侧边界，右侧边界。

花样变了一个又一个，每次我都是小心翼翼的去尝试，到底是用`left <= right` 还是 `left < right`, 还是`left = mid + 1` 还是 `left = mid`, 到底返回的是`left`还是`right`。

再经历过一次又一次的摸索与试错后，我决定打包搞一搞二分法，让这个小婊砸一次性服服帖帖。  

  
## 1.总体概述

**场景**：寻找一个数,寻找左边界，寻找右边界。

**难点**：循环条件带不带等号，更新边界要不要加一，返回数据要不要检查。

## 2.二分框架
```
def binarySearch(arr,target):
    left, right = 0,...
    while ...:
        mid = (l+r)//2
        if arr[mid] == target:
            ...
        elif arr[mid] < target:
            left = ...
        else:
            right = ...
    return ...
```
PS：最后的 else 可以写成 elif， 这样逻辑可以更清晰。 ```...``` 的部分是二分法的关键点，不同的情景需要不同的处理方式。


## 3.基本二分搜索

如果存在目标值，返回索引，如果不存在，返回-1。
```
def binarySearch(arr,target):
    left, right = 0,len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
**1. left和right的取值？**  

基本搜索时，目的是搜索目标值是否在数组中，左侧从0开始，右侧最后一个index是len(arr)-1，我们要搜索的index的范围是[0:len(arr)-1],保证每个要搜索的索引都不会index out of range。  

**2. 循环条件到底是 <= 还是 ==？**  

为什么循环条件是`left <= right` , 这意味着 `left == right + 1` 时循环终止，
举个例子，当 left == 2 时，搜索区间变成[3,2], 此区间为空，终止搜索，返回-1。 

如果循环条件是`left == right`, 意味着 `left == right` 时循环终止，
当left == 2时, 搜索区间变成[2,2], 终止搜索，但索引2并没有被检查，这时候返回-1是不对的。

如果条件选择为`left == right`， 我们需要在返回时多检查一下漏掉检查的index就可以。  

我们将源代码的最后一行进行一点改变，由
`return -1` 变成 `return left if arr[left] == target else -1`

**3. 怎么更新边界，left = mid + 1 还是 left = mid 或者 right = mid - 1 还是 right = mid ？**  

我们每次都是检查mid的数据，如果此索引上的值不是target，我们不需要再考虑这个索引了，所以 left = mid + 1, right = mid - 1, 这样就可以不再考虑此索引，也不会漏掉某些索引。


## 4.二分搜索左侧边界

首先，我们先明确一下左侧边界的定义。先看一些例子： 

对于数组`nums = [1,2,3,4]`,`target = 2`,左侧边界是`index = 1`;

对于数组`nums = [3,4,5,7]`,`target = 2`,左侧边界是`index = 0`;

对于数组`nums = [0,0,1,1]`,`target = 2`,左侧边界是`index = 4`;

可以发现，当我们求左侧边界的时候，其实我们找多少个数字小于`target`, 变种可以变为 **查找第一个值等于目标值的元素或位置** 和 **查找最后一个小于等于目标值的元素**

让我们先来看下搜索左侧边界的代码
```
def searchLeftBound(arr,target):
    if not arr:
        return -1
    left,right = 0,len(arr) 
    while left < right:
        mid = (left + right)//2
        if arr[mid] == target:
            right = mid    #注意
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid   #注意
     return left
```
**1.right的取值和循环条件**

这里right的取值是len(arr), 超出数组边界一个，意味着我们每次搜索的范围是左闭右开，[left,right), 而终止的条件是left == right, 当左右相等的时候，[left,right)自然为空，搜索可以停止。

那你会问，为什么搜索一个数用[left,right],但搜索边界的时候用[left,right)呢？其实上是因为这种写法比较普遍，我们当然也可以改写成跟搜索特定值的格式相同的代码块，会比这个更加的简单一些，后面我会把这几种情况一锅端。

**2.为什么是`left = mid + 1`,`right = mid`了呢？**

因为我们此时的搜索区间变成了[left,right), 当mid被检测了之后，下一次的搜索区间应该去掉mid，分成两个区间，他们是[left,mid)和[mid+1,right)。

**3.为什么可以用于搜索左边界？**

关键点在于处理 `arr[mid] == target`的方式，
```
if arr[mid] == target:
    right = mid 
```
我们每次找到了目标值，这次选择不返回，而是缩小搜索区间的right。

我们不是要搜索左边界么，就是要把整个搜索区间像左推，记住这个点就不容易写错了，当`arr[mid] == target`, `right = mid`把区间像左收缩，才能找到左边界。

**4.为什么返回left而不返回right？**

left,right其实都一样，因为循环的结束条件是`left == right`。

**5.能不能和之前的代码统一格式？**

多了一种代码模板就容易记错，那这个时候你可能想问，我们是不是可以统一到之前的代码格式呢？ **Of course!**

我想你们应该明白`<=` 和 `<` 的区别在于搜索区间是不是闭合的， `<=` 的区间是[left,right]，而`<`的区间则是[left,right)，我们当然可以统一他们。

现在我们想让区间两侧变成闭合的，那么在初始化left 和 right 的时候要 `left,right = 0,len(arr)-1`,这个时候循环终止条件变成 `left == right + 1`， 

退出while循环的条件变成了`left == right + 1`,我们想一下会有什么问题:

当target比所有数字都大的时候，right一直不变，left则向右一直推进，直到`left == right + 1`时退出循环，那么这个时候left == len(arr),引起索引越界。
因此，我们要在return之前进行判断看下left是否越界,我们看一下完整的代码:
```
def searchLeftBound(arr,target):
    if not arr:
        return -1
    left,right = 0,len(arr) - 1 
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            right = mid - 1    
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
    if left >= len(arr) or arr[left] != target:
        return -1
    return left
```
## 5.二分搜索右侧边界
搜索右侧边界的思想跟左侧很相似，只是有轻微的区别，废话不多说，我们先看一下代码吧。
```
def searchRightBound(arr,target):
    if not arr:
        return -1
    left,right = 0,len(arr) 
    while left < right:
        mid = (left + right)//2
        if arr[mid] == target:
            left = mid + 1    #注意
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid   #注意
     return left - 1
```

**1.怎么找到的右边界？**
关键点在于处理`arr[mid] == target`的方式
```
if arr[mid] == target:
    left = mid + 1
```
当我们找到arr[mid] = target的时候，我们向右侧缩小搜索空间，直到退出循环，最终锁定右边界。

**2.为什么返回的是`left-1`,而不是`left`或者 `right`？**
首先我们要明确的是，退出循环的条件是`left == right`,所以你也可以选择 `return right - 1`

那你又要问了，为什么要减1呢，因为当我们碰到`arr[mid] == target`的时候，采取的行动是`left = mid + 1`,当我们结束循环的时候，arr[left]不一定等于target了，但是arr[left-1]可能等于target。

这个时候你可能又要多嘴问那为啥更新是 `left = mid + 1` 而不是 `left = mid` 呢? 我就再不厌其烦的解释一下吧：

当`arr[mid] == target`时，我们要向右缩小搜索范围，此时的搜索范围是[left,right), 我们已经检查过mid了，那么向右的话就应该讲搜索范围变成[mid+1,right), 所以就是`left = mid + 1`。如果再不明白的话，请从头再理解一下二分法。

**3.返回-1的操作怎么办呢？**
如果target不在arr中，那我们最后需要检查一下left就好了。
```
if left == 0:
    return -1
return left - 1 if arr[left-1] == target else -1
```
**4.能不能统一格式？**
废话不多说，代码拿去吧。
```
def searchRightBound(arr,target):
    if not arr:
        return -1
    left,right = 0,len(arr)-1
    while left <=right:
        mid = (left + right)//2
        if arr[mid] == target:
            left = mid + 1    #注意
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 注意
     if right < 0 or arr[right] != target:
          return -1
     return right
```
当 target 比所有元素都小时，right 会被减到 -1，所以需要在最后防止越界。

## 6.逻辑统一
现在让我们统一三种二分的格式，全部使用[left,right]全闭的搜索区间来进行统一记忆，一次记他个乌漆嘛黑。

```
def binarySearch(arr,target):
    left, right = 0,len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
```
def binarySearchLeftBound(arr,target):
    left, right = 0,len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            right =  mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left >= len(arr) or arr[left] != target:
        return -1
    return left
```
```
def binarySearchRightBound(arr,target):
    left, right = 0,len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            right =  mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if right < 0 or arr[right] != target:
        return -1
    return right
```
是不是看到这已经对二分法豁然开朗，了然于胸。

我们只需要记住的是：

对于标准二分法，找到目标，return 目标。

对于找左边界， 找到目标，搜索区间向左推，即right = mid - 1, 最后看left是否超界。

对于找右边界，找到目标，搜索区间向右推，即left = mid + 1，最后看right是否超界。
