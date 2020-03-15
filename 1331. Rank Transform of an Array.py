class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ls = sorted(set(arr))
        dic = {}
        for i,num in enumerate(ls):
            dic[num] = i + 1
        
        for i,num in enumerate(arr):
            arr[i] = dic[num]
        return arr
            
