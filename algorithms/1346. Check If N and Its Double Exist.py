class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic = collections.Counter(arr)
        if dic[0] > 1:
            return True
        for n in dic:
            if n!= 0 and 2*n in dic:
                return True
        return False
