class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res, self.target = [], target
        for i in range(1,len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
        return res

    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num)+1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res)
                self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res)
                self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res)
                
                
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        results = []
        self.helper(num, 0, target, 0, 0, "", results)
        return results
    
    def helper(self, string, start, target, sum_so_far, last, path, results):
        if start == len(string) and sum_so_far == target:
            results.append(path)
        
        for end in range(start+1, len(string)+1):
            sub_string = string[start:end]
            if len(sub_string) > 1 and sub_string[0] == '0':
                break
            cur = int(sub_string)
            if start == 0:
                self.helper(string, end, target, sum_so_far + cur, cur, path + sub_string, results)
            else:
                self.helper(string, end, target, sum_so_far + cur, cur, path + "+" + sub_string, results)
                self.helper(string, end, target, sum_so_far - cur, -cur, path + "-" + sub_string, results)
                self.helper(string, end, target, sum_so_far - last + cur * last, cur * last, path + "*" + sub_string, results)
