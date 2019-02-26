## 1.search 

### List1  Combination
#### 17. Letter Combinations of a Phone Number 
1.dfs. From the first one to the last one. slowest speed.   
2.bfs. Add the ch layer by layer. Quickest speed.   
3.recursive. same as dfs, but from the last to the first.   
#### 39. Combination Sum
dfs. Remember the detai target and cur sum path, to check the list from little to large.   
#### 40. Combination Sum II
dfs. Each depth need to index + 1 but still care about skip the duplicate numbers.   
#### 77. Combinations
dfs. same as the combination 2 record the length, and each depth index+1.  
#### 78. Subsets   
1.dfs. same as combine.but no limit in length and append each time.  
2.bfs. look number as the layer, each layer add one number to previous all array.  
3.recursive. same as bfs, but use the one number add the recursive with num[:-1].  
#### 90. Subsets II
dfs. Only thing need to care is the duplicate skip.
#### 216. Combination Sum III
dfs. Thing need to care is the length k, decide k first and then target.   
    
### List2  Permutation
#### 46. Permutations   
dfs. The next depth nums need to delete the one which is added into the cur.   
#### 47. Permutations II
dfs. The next depth nums need to delete the one which is added into the cur, and also need to care the problem of repeat.   
#### 784. Letter Case Permutation
1.dfs. from the start to end, when meet alpha, split into two case, when get the end, add into array.   
2.bfs. space to start, and iter the String, when alpha,add two case into array.replace the array. it likes two for.   
3.Extend. put S in the array, iter it from 0 when alpha, extend the swapcase for each one.   
#### 996. Number of Squareful Arrays
dfs Same as the permutationII just need to add an additional condition to satify the square.  

### List3  Generate Parentheses
#### 22. Generate Parentheses
backtracking. Care about the number of left and right.   