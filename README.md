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




 

