# Algorithm

*Record the algorithm on leetcode depending on frequency.*

#### [*1.Two Sum ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/1.%20two%20sum.py)
>Use dictionary to save the reminder value and index.   
>Time: O(n), Space: O(n)

#### [*2.Add Two Numbers ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/2.%20Add%20Two%20Numbers.py)
>For two lists, add node by node and can use divmod function.   
>Time: O(n), Space: O(n)

#### [*3.Longest Substring Without Repeating Characters ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/3.%20Longest%20Substring%20Without%20Repeating%20Characters.py)
>Use dictionary to save the index of each char, if meet the char already in dic.  
>Make sure whether it appends before or afrer start position, update the start.   
>Compare length each time if add a new char in dic.   
>Time: O(n), Space: O(1)

#### [*146.LRU Cache ···*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/2.%20Add%20Two%20Numbers.py)
>Use a circle linked list to save the position of the nodes.   
>Use a dictionary to save the key -> Node(key,val).  
>Each get put the node after the root. Each reput val call the get.  
>Put need to check the cap. Need to del the node from the dic and linkedlist if needed.   
>Time: O(1)

#### [*4.Median of Two Sorted Arrays ···*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/4.%20Median%20of%20Two%20Sorted%20Arrays.py)
>Take the half of A(length i) and the other part of k is j = k - i from B.  
>Compare A[i] and B[j], if A[i] larger, find ith in A[:i] ,B[j:].  
>Make sure the total length of A and B is even or odd.  
>Time: O(log(m+n), Space: O(1)

#### [*200.Number of Islands ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/200.%20Number%20of%20Islands.py)
>Use dfs to detect each point is 1.  
>Time: O(m*n), Space: O(m*n)  

#### [*20.Valid Parentheses ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/20.Valid%20Parentheses.py)
>Use stack and dictionary.  
>Time: O(n), Space: O(n)  

#### [*5.Longest Palindromic Substring ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/5.%20Longest%20Palindromic%20Substring.py)
>For each char, detect the longest palidromic. Be careful of the odd and even.   
>Time: O(n2), Space: O(1) 

#### [*138.Copy List with Random Pointer ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/138.%20Copy%20List%20with%20Random%20Pointer.py)
>Use dictionary to create the same nodes first without the next and random point.  
>Iterate second time for the pointer.
>Time: O(n), Space: O(n) 

#### [*42.Trapping Rain Water ···*]()
>#### *TODO*

#### [*15.3Sum ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/15.%203Sum.py)
>Iterate each num in the array to find the other two nums with two pointers.  
>Time: O(n2), Space: O(n1) 


