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
 
