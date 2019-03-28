class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # if not rooms:
        #     return True
        # res = [0] * len(rooms)
        # res[0] = 1
        # def dfs(n):
        #     for key in rooms[n]:
        #         if res[key] == 0:
        #             res[key] = 1
        #             dfs(key)
        # dfs(0)
        # if 0 in res:
        #     return False
        # return True
        
        
        d = [0]
        open = set(d)
        while d:
            n = d.pop()
            for key in rooms[n]:
                if key not in open:
                    d.append(key)
                    open.add(key)
        return len(open) == len(rooms)

            
                
