class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return 0
        min_num = min(nums)
        max_num = max(nums)
        # 如果数组最大值最小值相等，则最大间距为0
        if min_num == max_num:
            return 0
        
        # 初始化三个长度为len(nums)+1的空数组，依次代表N+1个桶的信息。
        # bool_bkt：代表桶中是否存在元素。
        # min_bkt：代表对应桶中的最小元素。
        # max_bkt：代表对应桶中的最大元素。
        bool_bkt = [0]*(length+1) 
        min_bkt = [float('inf')]*(length+1)
        max_bkt = [-float('inf')]*(length+1)
        
        # 遍历数组，对于每个元素找到其对应的桶
        for i in range(length):
            bkt_idx = self.findBucket(nums[i], length, min_num, max_num)
            # 更新桶的标记位和对应的最大最小值
            if bool_bkt[bkt_idx] == 0:
                bool_bkt[bkt_idx] = 1
            if bool_bkt[bkt_idx] == 1:
                min_bkt[bkt_idx] = nums[i] if nums[i] < min_bkt[bkt_idx] else min_bkt[bkt_idx]
                max_bkt[bkt_idx] = nums[i] if nums[i] > max_bkt[bkt_idx] else max_bkt[bkt_idx]
       
        # 查找最大间距
        res = 0
        stack = []    # 依次存储包含元素的桶号
        if bool_bkt[0] == 1:
            stack.append(0)
        for i in range(1, length + 1):
            if bool_bkt[i] == 1:
                stack.append(i)
                if min_bkt[stack[-1]] - max_bkt[stack[-2]] > res:
                    res = min_bkt[stack[-1]] - max_bkt[stack[-2]]
            else:
                continue
        return res
     
    def findBucket(self, element, length, min_num, max_num):
        bkt_index = ((element - min_num) * length) // (max_num - min_num)
        return bkt_index
