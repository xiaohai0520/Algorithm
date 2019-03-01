class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if not target:
            return 0
        if '0000' in deadends:
            return -1
        res = 0
        deadends = set(deadends)
        queue = collections.deque([('0000',0)])
        visited = set()
        while queue:
            code,step = queue.popleft()
            
            if code == target:
                return step
            for code in self.gn(code):
                if code not in deadends and code not in visited:
                    queue.append((code,step+1))
                    visited.add(code)
            # if code in deadends:
            #     continue
            # for i in range(len(code)):
            #     num = int(code[i])
            #     # ls = []
            #     if num == 0:
            #         ls = [1,9]
            #     elif num == 9:
            #         ls = [0,8]
            #     else:
            #         ls = [num-1,num+1]
            #     for n in ls:
            #         newcode = code[:i] + str(n) + code[i+1:]
            #         if newcode not in deadends and newcode not in visited:
            #             queue.append((newcode,step+1))
        return -1
    
    def gn(self,combination):
        combo = list(map(int,list(combination)))
        return list(map(lambda x:''.join(map(str,x)), [combo[:i] + [(combo[i] + delta) %10 ] + combo[i+1:] for i in range(len(combination)) for delta in [-1,+1]]))
        
                
                
