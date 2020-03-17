class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        
        
        filtered_restaurants = []
        
        
        for restaurant in restaurants:
            if (veganFriendly):
                if (restaurant[2] and restaurant[3] <= maxPrice and restaurant[4] <= maxDistance):
                    filtered_restaurants.append(restaurant)
            elif (restaurant[3] <= maxPrice and restaurant[4] <= maxDistance):
                filtered_restaurants.append(restaurant)
            else:
                pass
            
        filtered_restaurants.sort(key = lambda x: (x[1], x[0], ), reverse = True)
        
        return [restaurant[0] for restaurant in filtered_restaurants]
        
        
        
        
        
#         dic = collections.defaultdict(list)
#         for r in restaurants:
#             if (veganFriendly == 0 or r[2] == 1) and r[3] <= maxPrice and r[4] <= maxDistance:
#                 dic[r[1]].append(r[0])
                
#         res = []
#         for key in sorted(dic.keys(),reverse=True):
#             # print(key)
#             # print(dic[key])
#             res.extend(sorted(dic[key],reverse=True))
#         return res
    
    
    
            
            
        
        
            
