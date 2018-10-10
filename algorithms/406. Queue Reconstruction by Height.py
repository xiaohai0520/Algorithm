#sort first by h and j   then insert by j

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []
        people.sort(key=lambda x:(-x[0],x[1]))
        res = [people[0]]
        for i in range(1,len(people)):
            h,index = people[i]
            res.insert(index,people[i])
        return res
