class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        res = [0] * n
        stack = []
        for x in logs:
            f_id, event, ts = x.split(':')
            f_id, ts = int(f_id), int(ts)
            if not stack or event == 'start':
                stack.append([f_id, ts])
            else:    
                duration = ts - stack.pop()[1] + 1
                res[f_id] += duration
                if stack: # remove nested calling's duration from parent function's duration
                    res[stack[-1][0]] -= duration
        return res
