#compare edges and dig

class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def dist(a, b):
            return (pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2)) ** 0.5

        points = [p1,p2,p3,p4]
        s = set()    
        plen = len(points)
        for i in range(plen):
            for j in range(i+1, plen):
                if points[i] == points[j]:
                    return False
                s.add(dist(points[i], points[j]))
        return  len(s) == 2        
