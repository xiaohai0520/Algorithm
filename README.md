# Algorithm

*Record the algorithm on leetcode depending on frequency.*

#### 1-[*1.Two Sum ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/1.%20two%20sum.py)
>Use dictionary to save the reminder value and index.   
>Time: O(n), Space: O(n)

#### 2-[*2.Add Two Numbers ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/2.%20Add%20Two%20Numbers.py)
>For two lists, add node by node and can use divmod function.   
>Time: O(n), Space: O(n)

#### 3-[*3.Longest Substring Without Repeating Characters ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/3.%20Longest%20Substring%20Without%20Repeating%20Characters.py)
>Use dictionary to save the index of each char, if meet the char already in dic.  
>Make sure whether it appends before or afrer start position, update the start.   
>Compare length each time if add a new char in dic.   
>Time: O(n), Space: O(1)

#### 4-[*146.LRU Cache ···*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/2.%20Add%20Two%20Numbers.py)
>Use a circle linked list to save the position of the nodes.   
>Use a dictionary to save the key -> Node(key,val).  
>Each get put the node after the root. Each reput val call the get.  
>Put need to check the cap. Need to del the node from the dic and linkedlist if needed.   
>Time: O(1)

#### 5-[*4.Median of Two Sorted Arrays ···*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/4.%20Median%20of%20Two%20Sorted%20Arrays.py)
>Take the half of A(length i) and the other part of k is j = k - i from B.  
>Compare A[i] and B[j], if A[i] larger, find ith in A[:i] ,B[j:].  
>Make sure the total length of A and B is even or odd.  
>Time: O(log(m+n), Space: O(1)

#### 6-[*200.Number of Islands ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/200.%20Number%20of%20Islands.py)
>Use dfs to detect each point is 1.  
>Time: O(m*n), Space: O(m*n)  

#### 7-[*20.Valid Parentheses ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/20.Valid%20Parentheses.py)
>Use stack and dictionary.  
>Time: O(n), Space: O(n)  

#### 8-[*5.Longest Palindromic Substring ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/5.%20Longest%20Palindromic%20Substring.py)
>For each char, detect the longest palidromic. Be careful of the odd and even.   
>Time: O(n2), Space: O(1) 

#### 9-[*138.Copy List with Random Pointer ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/138.%20Copy%20List%20with%20Random%20Pointer.py)
>Use dictionary to create the same nodes first without the next and random point.  
>Iterate second time for the pointer.
>Time: O(n), Space: O(n) 

#### 10-[*42.Trapping Rain Water ···*]()
>#### *TODO*

#### 11-[*15.3Sum ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/15.%203Sum.py)
>Iterate each num in the array to find the other two nums with two pointers.  
>Time: O(n2), Space: O(n1) 

#### 12-[*11.Container With Most Water ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/11.%20Container%20With%20Most%20Water.py)
>Search with two pointers from two sides.  
>Time: O(n), Space: O(n1) 

#### 13-[*7.Reverse Integer ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/7.%20Reverse%20Integer.py)
>Use divmod.  
>Time: O(n), Space: O(n1) 

#### 14-[*141.Linked List Cycle ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/141.%20Linked%20List%20Cycle.py)
>Use two pointer fast and slow.  
>Time: O(n), Space: O(n1) 

#### 15-[*56.Merge Intervals ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/56.%20Merge%20Intervals.py)
>Sort firstly. Add into the array one by one. If start < end, merge.  
>Time: O(n), Space: O(n) 

#### 16-[*121.Best Time to Buy and Sell Stock ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock.py)
>Update the miniprice all the time and update the maxprofit.   
>Time: O(n), Space: O(1) 

#### 17-[*53.Maximum Subarray ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/53.%20Maximum%20Subarray.py)
>Dp record the max all the time or record each day max.  
>Time: O(n), Space: O(1) 

#### 18-[*21.Merge Two Sorted Lists ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/21.%20Merge%20Two%20Sorted%20Lists.py)
>Use dummy node to next node. 
>Time: O(n), Space: O(1) 

#### 19-[*206.Reverse Linked List ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/206.%20Reverse%20Linked%20List.py)
>Use pre. Start pre is None.  
>Time: O(n), Space: O(n) 

#### 20-[*23.Merge k Sorted Lists ···*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/23.%20Merge%20k%20Sorted%20Lists.py)
>Use deque to save all lists firstly.  
>Each time pop two lists and merge them until only one lists in the deque.  
>Time: O(n2), Space: O(n) 

#### 21-[*238.Product of Array Except Self ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/238.%20Product%20of%20Array%20Except%20Self.py)
>Each position is equal the left time the right. Iterate two times, from left to right and reverse.   
>Time: O(n), Space: O(n) 

#### 22-[*771.Jewels and Stones ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/771.%20Jewels%20and%20Stones.py)
>Iterate each char in S to find whether in J.   
>Time: O(n2), Space: O(1) 

#### 23-[*9.Palindrome Number ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/9.%20Palindrome%20Number.py)
>Make the reverse number and find if they are same.  
>Time: O(n), Space: O(1) 

#### 24-[*301.Remove Invalid Parentheses ···*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/301.%20Remove%20Invalid%20Parentheses.py)
>Make sure how to find the invalid parenthess.  
>Try each possible of step one.  
>Time: O(n2), Space: O(n) 

#### 25-[*344.Reverse String ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/344.%20Reverse%20String.py)
>To list and reverse from both sides.  
>Time: O(n), Space: O(n) 

#### 26-[*17.Letter Combinations of a Phone Number ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/17.%20Letter%20Combinations%20of%20a%20Phone%20Number.py)
>Use dfs to add each layer number map char.  
>Time: O(2n), Space: O(n) 

#### 27-[*681.Next Closest Time ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/681.%20Next%20Closest%20Time.py)
>Add one minute to try the new time. whether each char in the set.   
>Time: O(n), Space: O(1) 

#### 28-[*33.Search in Rotated Sorted Array ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/33.%20Search%20in%20Rotated%20Sorted%20Array.py)
>Use binary search. Make sure which is rotate.   
>Time: O(logn), Space: O(n) 

#### 29-[*253.Meeting Rooms II ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/253.%20Meeting%20Rooms%20II.py)
>Sort with the start time.Use heapq to keep the smallest end time in the front.  
>If the start time larger than first end time in heapq, replace else add into heapq.  
>Time: O(n), Space: O(n) 

#### 30-[*139.Word Break ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/139.%20Word%20Break.py)
>Use the dp to save each point in the string. Check dp -1.   
>Time: O(n), Space: O(n)

#### 31-[*31.Next Permutation ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/31.%20Next%20Permutation.py)
>From tail to head, find the first number decrease.   
>Replace with the first larger number than that one. Reverse the last part.   
>Time: O(n), Space: O(1)

#### 32-[*297.Serialize and Deserialize Binary Tree ···*]()
>#### *TODO*   

#### 33-[*482.License Key Formatting ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/482.%20License%20Key%20Formatting.py)
>Find the reminder part at first.    
>Time: O(n), Space: O(1)

#### 34-[*13.Roman to Integer ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/13.%20Roman%20to%20Integer.py)
>If the one small than next one. minus it val.   
>Time: O(n), Space: O(1)

#### 35-[*22.Generate Parentheses ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/22.%20Generate%20Parentheses.py)
>Use dfs to add parentheses.   

#### 36-[*76.Minimum Window Substring ···*]()
>#### *TODO*   

#### 37-[*88.Merge Sorted Array ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/88.%20Merge%20Sorted%20Array.py)
>From tail to head.  
>Time: O(n), Space: O(1)

#### 38-[*54.Spiral Matrix ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/54.%20Spiral%20Matrix.py)
>Use while loop to add number into array. Be careful of the edge.  
>Time: O(n2), Space: O(n2)


#### 39-[*819.Most Common Word ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/819.%20Most%20Common%20Word.py)
>Regular expression to split the line. Dictionary to save the times of each word.  
>Time: O(n), Space: O(n)

#### 40-[*283.Move Zeroes ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/283.%20Move%20Zeroes.py)
>Two pointers to record the first zero and all number.  
>Time: O(n), Space: O(n)

#### 41-[*695.Max Area of Island ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/695.%20Max%20Area%20of%20Island.py)
>Use dfs to cal the area of each land. Get the max one.  
>Time: O(n2), Space: O(1)

#### 42-[*412.Fizz Buzz ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/412.%20Fizz%20Buzz.py)
>Not 0 is 1, not number is 0 to times fizz.   
>Time: O(n), Space: O(1)

#### 43-[*547.Friend Circles ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/547.%20Friend%20Circles.py)
>To find each person and use an array to record visit state.    
>Time: O(n2), Space: O(n)

#### 44-[*49.Group Anagrams ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/49.%20Group%20Anagrams.py)
>Use tuple of each sorted str as key to save in the dictionary.    
>Time: O(n), Space: O(n)

#### 45-[*904.Fruit Into Baskets ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/904.Fruit%20Into%20Baskets.py)
>Sliding window. It is find the max subarray with two elements.     
>Time: O(n), Space: O(n)

#### 46-[*289.Game of Life  ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/289.Game%20of%20Life.py)
>Get the neighbor state of each point and try to save them in place.  Then change the state one by one.    
>Time: O(n2), Space: O(1)

#### 47-[*91.Decode Ways  ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/91.%20Decode%20Ways.py)
>Use dp to record each step number.   
>Time: O(n), Space: O(1)

#### 48-[*151.Reverse Words in a String  ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/151.%20Reverse%20Words%20in%20a%20String.py)
>Change to list and get the reverse.join together.   
>Time: O(n), Space: O(n)

#### 49-[*8.String to Integer (atoi) ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/8.%20String%20to%20Integer%20(atoi).py) 
>Time: O(n), Space: O(n)

#### 50-[*98.Validate Binary Search Tree  ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/98.%20Validate%20Binary%20Search%20Tree.py)
>Use in order to find the smallest one then compare with the second smallest one.   


#### 51-[*347.Top K Frequent Elements  ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/347.%20Top%20K%20Frequent%20Elements.py)
>Counter to save the times of number then sort by times.   
>Time: O(n), Space: O(n)

#### 52-[*16.3Sum Closest  ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/16.%203Sum%20Closest.py)
>Like three sum. two pointers to get the minimum ads different.    
>Time: O(n2), Space: O(1)

#### 53-[*50.Pow(x, n)  ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/50.%20Pow(x,%20n).py)
>Take care the bound when n = 0 and n = 1.    
>Time: O(logn), Space: O(1)

#### 54-[*929.Unique Email Addresses ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/929.Unique%20Email%20Addresses.py)
>split and replace and set and index.    
>Time: O(n), Space: O(n)

#### 55-[*173.Binary Search Tree Iterators ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/173.%20Binary%20Search%20Tree%20Iterator.py)
>Use a stack just save the tree left, like inorder.   
>Time: O(1), Space: O(logn)

#### 56-[*236.Lowest Common Ancestor of a Binary Tree ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/236.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree.py)
>Use recursive to find node.    

#### 57-[*25.Reverse Nodes in k-Group  ···*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/25.%20Reverse%20Nodes%20in%20k-Group.py)
>Reverse one part then recursive to reverse next part.  
>Time: O(n), Space: O(1)

#### 58-[*127.Word Ladder  ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/127.%20Word%20Ladder.py)
>Bfs to search the least path.  
>Time: O(mn), Space: O(mn)

#### 59-[*46.Permutations ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/46.%20Permutations.py)
>Dfs

#### 60-[*399.Evaluate Division   ··*]()
>#### Graph. *TODO*

#### 61-[*79.Word Search  ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/79.%20Word%20Search.py)
>Dfs and need to backtracking the previous chr in the matrix.

#### 62-[*300.Longest Increasing Subsequence  ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/300.Longest%20Increasing%20Subsequence.py)
>Dp array to remember each step the max length use iterate previous ones.  
>Time: O(n2), Space: O(n)

#### 63-[*70.Climbing Stairs  ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/70.%20Climbing%20Stairs.py)
>Dp.    
>Time: O(n), Space: O(n)

#### 64-[*535.Encode and Decode TinyURL ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/535.%20Encode%20and%20Decode%20TinyURL.py)
>Use dic and choice() to get and save the url.      
>Time: O(n), Space: O(n)

#### 65-[*41.First Missing Positive  ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/41.%20First%20Missing%20Positive.py)
>Array. index as the hash value.     
>Time: O(n), Space: O(1)

#### 66-[*224	Basic Calculator  ···*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/224.%20Basic%20Calculator.py)
>Stack to save ().      
>Time: O(n), Space: O(1)

#### 67-[*215.Kth Largest Element in an Array  ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/215.%20Kth%20Largest%20Element%20in%20an%20Array.py)
>Quick select.      
>Time: O(n), Space: O(n)

#### 68-[*14.Longest Common Prefix ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/14.%20Longest%20Common%20Prefix.py)
>Use the shortest one to compare each word.      
>Time: O(n), Space: O(1)

#### 69-[*67.Add Binary ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/67.%20Add%20Binary.py)
>Same to linked list add.      
>Time: O(n), Space: O(n)

#### 70-[*560.Subarray Sum Equals K ··*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/560.%20Subarray%20Sum%20Equals%20K.py)
>Dic to save each sum times and find the reminder is num to add count.      
>Time: O(n), Space: O(n)

#### Tree---------------------------------------

#### 71-[*226.Invert Binary Tree ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/226.%20Invert%20Binary%20Tree.py)
>Recursive BFS or DFS to solve.    

#### 72-[*617.Merge Two Binary Trees ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/617.%20Merge%20Two%20Binary%20Trees.py)
>Recursive.   

#### 73-[*700.Search in a Binary Search Tree  ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/700.Search%20in%20a%20Binary%20Search%20Tree.py)
>Recursive.  

#### 74-[*590.N-ary Tree Postorder Traversal.py ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/590.N-ary%20Tree%20Postorder%20Traversal.py)
>Recursive or use stack to do reverse res at last.   

#### 75-[*589.N-ary Tree Preorder Traversal ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/589.N-ary%20Tree%20Preorder%20Traversal.py)
>Recursive or use stack to do reverse res at last. 

#### 76-[*559.Maximum Depth of N-ary Tree ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/559.Maximum%20Depth%20of%20N-ary%20Tree.py)
>    

#### 77-[*559.Maximum Depth of N-ary Tree ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/559.Maximum%20Depth%20of%20N-ary%20Tree.py)
>  

#### 78-[*559.Maximum Depth of N-ary Tree ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/559.Maximum%20Depth%20of%20N-ary%20Tree.py)
>  

#### 79-[*104.Maximum Depth of Binary Tree ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/104.%20Maximum%20Depth%20of%20Binary%20Tree.py)
>   

#### 80-[*872.Leaf-Similar Trees ·*](https://github.com/xiaohai0520/Algorithm/blob/master/algorithms/872.Leaf-Similar%20Trees.py)
>  

