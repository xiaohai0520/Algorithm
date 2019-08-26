class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        def frac(x,y):
            g = gcd(x,y)
            return x//g, y//g
        
        l = len(points)
        m = 0
        for i in range(l):
            dic = {'i': 1}
            same = 0
            for j in range(i+1, l):
                tx, ty = points[j][0], points[j][1]
                dx = points[i][0]-tx
                dy = points[i][1]-ty
                
                if dx == 0 and dy == 0:  # same point 
                    same += 1
                    continue
                if dx == 0 :           # y axis
                    slope = 'i'
                else:
                    slope = frac(dx, dy)  
                if slope not in dic: 
                    dic[slope] = 1
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)
        return m
        
        
        
        
        # l = len(points)
        # m = 0
        # for i in range(l):
        #     dic = {'i': 1}
        #     same = 0
        #     for j in range(i+1, l):
        #         tx, ty = points[j][0], points[j][1]
        #         if tx == points[i][0] and ty == points[i][1]: 
        #             same += 1
        #             continue
        #         if points[i][0] == tx: 
        #             slope = 'i'
        #         else:
        #             slope = (points[i][1]-ty) * 1.0 /(points[i][0]-tx)
        #         if slope not in dic: 
        #             dic[slope] = 1
        #         dic[slope] += 1
        #     m = max(m, max(dic.values()) + same)
        # return m
