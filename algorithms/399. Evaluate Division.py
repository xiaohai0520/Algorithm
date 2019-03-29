class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = collections.defaultdict(list)
        for equation, value in zip(equations, values):
            num, den = equation
            g[num].append((den, value))
            g[den].append((num, 1.0/value))
            
        res = []
        
        def calc(num, den):
            if num not in g or den not in g:
                return -1.0
            queue = [(num, 1.0)]
            seen = set()
            while queue:
                numerator, value = queue.pop(0)
                if numerator == den:
                    return value
                seen.add(numerator)
                for nei, val in g[numerator]:
                    if nei not in seen:
                        queue.append((nei, value * val))

            return -1.0
                            
        for num, den in queries:
            ans = calc(num, den)
            res.append(ans)
        
        return res
            
