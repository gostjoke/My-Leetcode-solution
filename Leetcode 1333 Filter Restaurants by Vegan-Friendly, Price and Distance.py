'''
07/12/2023
'''

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans= []
        for i in range(len(restaurants)):
            if restaurants[i][2] >= veganFriendly and restaurants[i][3] <= maxPrice and restaurants[i][4] <= maxDistance:
                ans.append(restaurants[i])

        ans.sort(key=lambda x:x[0], reverse=True)
        ans.sort(key=lambda x:x[1], reverse=True)
        
        return [x[0] for x in ans]
