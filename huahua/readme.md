## 1.search 

### List1  
#### 17. Letter Combinations of a Phone Number 
(review: 1.(5)forget the empty situation)   
1.dfs. From the first one to the last one. slowest speed.   
2.bfs. Add the ch layer by layer. Quickest speed.   
3.recursive. same as dfs, but from the last to the first.   
#### 39. Combination Sum
(review: 1.(10) forget the start point    
dfs. Remember the detai target and cur sum path, to check the list from little to large.   
#### 40. Combination Sum II
(review 1.(3) forget the avoid repeat)    
dfs. Each depth need to index + 1 but still care about skip the duplicate numbers.   
#### 77. Combinations
(review 1.(6) early stop wrong   
dfs. same as the combination 2 record the length, and each depth index+1.  
#### 78. Subsets
(review 1.(5) perfect   
1.dfs. same as combine.but no limit in length and append each time.  
2.bfs. look number as the layer, each layer add one number to previous all array.  
3.recursive. same as bfs, but use the one number add the recursive with num[:-1].  
#### 90. Subsets II
(review 1(3) perfect  
dfs. Only thing need to care is the duplicate skip.
#### 216. Combination Sum III
(review 1(4) perfect 
dfs. Thing need to care is the length k, decide k first and then target.   
    
### List2 
#### 46. Permutations  
(review 1(3) perfect
dfs. The next depth nums need to delete the one which is added into the cur.   
#### 47. Permutations II
(review 1(No) not know how to avoid the duplicate.  
dfs. The next depth nums need to delete the one which is added into the cur, and also need to care the problem of repeat.   
#### 784. Letter Case Permutation
(review 1(No)..
1.dfs. from the start to end, when meet alpha, split into two case, when get the end, add into array.   
2.bfs. space to start, and iter the String, when alpha,add two case into array.replace the array. it likes two for.   
3.Extend. put S in the array, iter it from 0 when alpha, extend the swapcase for each one.   
#### 996. Number of Squareful Arrays
(review 1(No) dfs need to avoid duplicate and use used array.  
dfs Same as the permutationII just need to add an additional condition to satify the square.  

### List3  
#### 22. Generate Parentheses
(review 1(2) perfect)    
backtracking. Care about the number of left and right.   
#### 301. Remove Invalid Parentheses
(review 1(No) count delete dfs  
1.Force. We can find all possible to use filter to choose the valid ones.
2.dfs. Count the left more and right more first. and use dfs to try from head to tail.   

### List4 
#### 37. Sudoku Solver  
(review 1(NO)  solve recursive until not empty 
check three conditions and use the dfs to sovle check one by one.   
#### 51. N-Queens
(review 1(No))  
Also use the dfs backtracking from row to row, in each row check col and diag.   
#### 52. N-Queens II
(review 1(No))  
Same as 51, just need to count the number.   

### List5 
#### 79. Word Search
(review 1(3) perfect)  
use dfs to check very word[0]    
#### 212. Word Search II
(review 1(No) Trie tree
Using trie tree to do the dfs search.   

### List6 
#### 127. Word Ladder
(review 1(5) perfect use bfs and queue.
BFS use queue to save the word and length. Then pop left to get the tuple.  
#### 126. Word Ladder II
(review 1(No) 
BFS  search layer by layer, use the default dic to save the list, key is the last word in the list, it means the path, if the word is endword, append to the res.   
BiBFS same as BFS but use the forword and backword, if word in for in the back or back in the for it means meeting ,can combine together.    
#### 752. Open the Lock
(review 1(dfs)
BFS not forget to add a set to save the visited.   
#### 542. 01 Matrix

DFS. get the mini one but it will cost more time.   
BFS. try to search layer by layer.   
#### 934. Shortest Bridge
DFS to search the island, BFS to get the shortest path.  

### List7 
#### 698. Partition to K Equal Sum Subsets
dfs. set k block to fill. iterative each index until to the last one, else return false.   
#### 93. Restore IP Addresses
DFS try each 1 -3 combinations to add to the ip ,if k >4 return.   
#### 131. Palindrome Partitioning
DFS check each possible of the substring whether it is a palindrom, if not s , join it into the res.    
#### 241. Different Ways to Add Parentheses
Divide and conquer. split the st to left and right, get two array of nums, add each op into the res.   
#### 842. Split Array into Fibonacci Sequence 
DFS and backtracking. dfs from the start to the end ,if index == len(s) return true. fit the condition add number into array, else ,pop() and return false.  

## 2.DP

### List1 
#### 70. Climbing Stairs 
dp. pre one and two to add together.  
#### 746. Min Cost Climbing Stairs
dp same as 70 need to add the cost.  

### List2
#### 303. Range Sum Query - Immutable
DP. use the dp array record all the sum from 0 to i.   

### List3
#### 53. Maximum Subarray
Dp easy to solve, divide and conquer, split from middle, and get the left continous and right contious largest, compare with maxleft and right max.   
#### 121. Best Time to Buy and Sell Stock
dp  always save the maxprofit, and find the minvalue use the price to minus the min to compare the max value.   

### List4  
#### 198. House Robber  
dp, the dp i-1 or dp[i-2] + nums[i] larger.   
#### 213. House Robber II
just two dp without first or last , compare to get the larger.   
#### 309. Best Time to Buy and Sell Stock with Cooldown
Hard question three conditions, sold hold and rest, find the relationship between both of them.   
#### 740. Delete and Earn
same as house robber,you can think each house is the index of total number, translate into the robber style and do the dp.  
#### 801. Minimum Swaps To Make Sequences Increasing
two array to remember the state of swap and non swap. good question. 

### List5
#### 139. Word Break
dp to record the boolean of each index  
#### 140. Word Break II
check can be devided and use dfs to add the word into the array.   

### List6
#### 300. Longest Increasing Subsequence
dp record the previous nums the longest lengh if large than the length, add 1.  
#### 673. Number of Longest Increasing Subsequence
two dp arrays, one saves longest one and one saves longest one number.   

### !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!DP TO DO  

## 3.TREE
### List1
#### 94. Binary Tree Inorder Traversal
(review sb)
#### 144. Binary Tree Preorder Traversal
(review 1 p  
#### 145. Binary Tree Postorder Traversal
(review 1 p
#### 589. N-ary Tree Preorder Traversal
(review 1 p
#### 590. N-ary Tree Postorder Traversal
(review 1 p
#### 572. Subtree of Another Tree
(review 1 p 

### List2
#### 100. Same Tree
#### 101. Symmetric Tree
#### 104. Maximum Depth of Binary Tree
#### 110. Balanced Binary Tree
#### 111. Minimum Depth of Binary Tree
#### 965. Univalued Binary Tree

### List3
#### 102. Binary Tree Level Order Traversal
#### 107. Binary Tree Level Order Traversal II
#### 429. N-ary Tree Level Order Traversal
#### 872. Leaf-Similar Trees
#### 987. Vertical Order Traversal of a Binary Tree

### List4
#### 814. Binary Tree Pruning
#### 669. Trim a Binary Search Tree

### List5
#### 112. Path Sum
#### 113. Path Sum II
#### 437. Path Sum III

### List6
#### 124. Binary Tree Maximum Path Sum
dfs to iterative the tree and update the max value all the time, return max(left,right) + val   
#### 543. Diameter of Binary Tree
same as the previous item    
#### 687. Longest Univalue Path

### List7
#### 129. Sum Root to Leaf Numbers
bfs to save 10*layer + val   
dfs get all number and sum together
#### 257. Binary Tree Paths

### List8
#### 236. Lowest Common Ancestor of a Binary Tree
#### 235. Lowest Common Ancestor of a Binary Search Tree

### List9
#### 449. Serialize and Deserialize BST
#### 297. Serialize and Deserialize Binary Tree

### List10
#### 508. Most Frequent Subtree Sum

### List11
#### 968. Binary Tree Cameras
from the down to the up to see the node type.  (0,1,2)
#### 979. Distribute Coins in Binary Tree
same as the previous one. from leaf to root.   
#### 337. House Robber III
dp and tree. return no_choose and choose and return the larger one.   

## 4.Binary Search
### List1
#### 35. Search Insert Position
#### 34. Find First and Last Position of Element in Sorted Array
when search the right bound, mid = l + r // 2 + 1 can avoid dead loop.   
#### 704. Binary Search
#### 981. Time Based Key-Value Store
use defaultdict(list) and bisect to seach the bound.   

### List2
#### 33. Search in Rotated Sorted Array
#### 81. Search in Rotated Sorted Array II
delete duplicate first of the l and r.   
#### 153. Find Minimum in Rotated Sorted Array
#### 154. Find Minimum in Rotated Sorted Array II


### List3
#### 69. Sqrt(x)
#### 74. Search a 2D Matrix
think of a whole line and use the binary search.   
#### 378. Kth Smallest Element in a Sorted Matrix
#### 719. Find K-th Smallest Pair Distance
#### 875. Koko Eating Bananas

## 5.BST
### List1
#### 98. Validate Binary Search Tree
#### 783. Minimum Distance Between BST Nodes
#### 530. Minimum Absolute Difference in BST
#### 700. Search in a Binary Search Tree
#### 701. Insert into a Binary Search Tree
#### 230. Kth Smallest Element in a BST
#### 99. Recover Binary Search Tree
