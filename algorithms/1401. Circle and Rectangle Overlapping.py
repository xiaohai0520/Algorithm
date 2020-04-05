class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        rx = (x2 + x1)/2
        ry = (y2 + y1)/2
        distance = ((rx-x_center)**2 + (ry - y_center)**2) **0.5
        #print(distance)
        
        tr = ((rx-x1)**2 + (ry - y1)**2)**0.5
        
        
        t = tr + radius
        #print(t)
        if distance <= t:
            return True
        return False
        
