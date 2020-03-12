class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        m = len(mat)
        n = len(mat[0])
        for x in range(m):
            for y in range(n):
                dic[x-y].append(mat[x][y])
        #print(dic)
        
        for k,v in dic.items():
            dic[k] = sorted(v,reverse=True)
        for r,row in enumerate(mat):
            for c,ele in enumerate(row):
                mat[r][c] = dic[r-c].pop()
        return mat
