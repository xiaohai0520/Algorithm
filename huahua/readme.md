## 1.search  
### List1  
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
