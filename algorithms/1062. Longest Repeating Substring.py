class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        
        def search(length):
            seen = set()
            for i in range(len(S)-length+1):
                if S[i:i+length] in seen:
                    return True
                seen.add(S[i:i+length])
            return False
        left, right = 1, len(S)
        while left <= right:
            mid = left + (right - left) // 2
            if search(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1
        
        
        
        
        
#         if not S:
#             return 0
#         dp = [[0 for _ in range(len(S))] for _ in range(len(S))]
        
#         for i in range(len(S)):
#             for j in range(i+1,len(S)):
#                 if S[i] == S[j]:
#                     dp[i][j] = dp[i-1][j-1] + 1
#                 else:
#                     dp[i][j] = 0
#         return max([max(ls) for ls in dp])
        
        
        
        
        
        
        
        
        
        # dic = {}
        # for i in range(len(S)):
        #     for j in range(i,len(S)):
        #         dic[S[i:j+1]] = dic.get(S[i:j+1],0) + 1
        #         # print(S[i:j+1],dic[S[i:j+1]])
        # res = 0
        # for key in dic:
        #     if len(key) > res and dic[key] > 1:
        #         res = len(key)
        # return res
