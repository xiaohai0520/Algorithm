# TOP 100 QUESTIONS ON LEETCODE

## No.1 : [Two Sum](https://leetcode.com/problems/two-sum/)  
**Array and dictionary**.  
Using dictionary to save the target and make the time complexity is O(n).   
Using the enumerate to iterate the numbers array.    

## No.2 : [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)  
**LinkedList**.  
Using divmod to get the value and carry.  
If no value but carry, continue to add the carry to the list.  

## No.3 : [LRU Cache](https://leetcode.com/problems/lru-cache/)   
**Data Structure for linked list and dictionary**.  
Using dictionary to complete finding and saving node in O(1) time.  
We can also use the API [OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict) to apply this.  
OrderedDict includes methods: popitem(last=True) and move_to_end(key, last=True).

## No.4 : [Number of Islands](https://leetcode.com/problems/number-of-islands/)   
**DFS and BFS**.   
Iterate each position in the array, if is 1 to dfs or bfs this node until can not continue.  

## No.5 : [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)   
**String and dictionary**.   
Save the index of each char of the string into dictionary.  
Find the repeat position and let start index plus 1.  
 
## No.6 : [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)   
**Binary Search, Divide and Conquer**.   
Because two arrays are in the sequence. We can think this problem to find the kth number.
Divide the short one into two parts and get the other part from the array. Compare the middle value.

## No.7 : [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)   
**Two pointers**.   
Try from two sides and always update the lower one.   

## No.8 : [3Sum](https://leetcode.com/problems/3sum/)   
**Two pointers**.   
Similiar with the previous one. Try from two sides and avoid the repeat.  

## No.9 : [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)   
**BFS and DFS**.   
BFS. For each digit then try to add each possible.
DFS. From the first digit to the last digit to try each possible.  

## No.10 : [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)   
**Linked List and Two pointers**.   
Use two pointers to complete in one pass.   
Add a dummy node to save the head and also not need to care the delete the head.   

## No.11 : [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)   
**Stack and Dictionary**.   
Use stack to save the first part of parenthese and pop to compare the second part.   

## No.12 : [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)   
**DFS**.   
Count the two part of the paremtheses and if left > right need to return.  

## No.13 : [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)   
**Deque and linked list**.   
Pop the first two list to merge into one and insert into the deque again.  
Until there is only one element in the queue.  






