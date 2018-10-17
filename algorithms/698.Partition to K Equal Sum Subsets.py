class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        stack = []
        for num in nums:
            if not stack or num == stack[-1] + 1:
                stack.append(num)
            else:
                cur = ''
                if len(stack) > 1:
                    cur = str(stack[0]) + '->' +str(stack[-1])
                else:
                    cur = str(stack[0])
                res.append(cur)
                stack = [num]
                
        if len(stack) > 1:
            res.append(str(stack[0]) + '->' +str(stack[-1]))
        else:
            res.append(str(stack[0]))

                
        return res
                
