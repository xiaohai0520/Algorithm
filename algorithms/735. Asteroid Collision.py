#use stack
class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = []
        for asteroid in asteroids:
            if len(res) == 0 or asteroid > 0:
                res.append(asteroid)
            elif asteroid < 0:
                # While top of the stack is positive.
                while len(res) and res[-1] > 0:
                    # Both asteroids are equal, destroy both.
                    if res[-1] == -asteroid: 
                        res.pop()
                        break
                    # Stack top is smaller, remove the +ve asteroid 
                    # from the stack and continue the comparison.
                    elif res[-1] < -asteroid:
                        res.pop()
                        continue
                    # Stack top is larger, -ve asteroid is destroyed.
                    elif res[-1] > -asteroid:
                        break
                else:
                    # -ve asteroid made it all the way to the 
                    # bottom of the stack and destroyed all asteroids.
                    res.append(asteroid)
        return res
