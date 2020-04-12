# Leetcode Binary Search problems 

## Find Bound
很多问题都可以转换为查找左边界或者查找右边界，这里面又需要考虑查找的值是不是在数组中，还是单纯的找出最后一个小于目标值(左边界)或者第一个大于目标值](右边界)。

|#|Title|Solution|Difficulty|
|---|-----|--------|----------|
|1337|[The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/)|[Python](../algorithms/1337.%20The%20K%20Weakest%20Rows%20in%20a%20Matrix.md)|Easy|

## Sorted Matrix
二分查找经常会用在一维的数组中，当一个二维的矩阵的行和列也是单调排列的时候，我们这个时候也是可以考虑二分法的。
这类题的解法往往都是从矩阵的左下角或者右上角开始搜索，每次进行行更新或者列更新，直到矩阵的另外一个对角结束。
 
|#|Title|Solution|Difficulty|
|---|-----|--------|----------|
|1351|[Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)|[Python](../algorithms/1351.%20Count%20Negative%20Numbers%20in%20a%20Sorted%20Matrix.md)|Easy|
