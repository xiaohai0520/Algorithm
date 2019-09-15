class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        line, result = int(math.log(label, 2)), [label]
        
        while line:            
		    # calculate offset to the left or right side
            offset = result[-1] - 2 ** line
			# subtract current offset and parent offset
            result.append(result[-1] - offset - (offset // 2 + 1))
            line -= 1
            
        return result[::-1]
