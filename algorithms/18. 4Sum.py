用递归的方式 逐渐的讲4sum 变成3sum 最后变成2sum

每次都有左右两个边界，然后从左边界开始 逐步的查询，

每次在target上减去 当前的数字，知道变成2sum为止，

如果2sum的和为target 则将这种结果加入数组

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def find(l,r,target,N,result):
            if N == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l,r+1):
                    if i > l and nums[i] == nums[i-1]:
                        continue
                    find(i+1,r,target-nums[i],N-1,result+[nums[i]])
        
        nums.sort()
        results = []
        find(0,len(nums)-1,target,4,[])
        return results
        


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        d = dict()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum2 = nums[i]+nums[j]
                if sum2 in d:
                    d[sum2].append((i,j))
                else:
                    d[sum2] = [(i,j)]
        
        result = set()
        for key in d:
            value = target - key
            if value in d:
                list1 = d[key]
                list2 = d[value]
                for (i,j) in list1:
                    for (k,l) in list2:
                        if i!=k and i!=l and j!=k and j!=l:
                            flist = [nums[i],nums[j],nums[k],nums[l]]
                            flist.sort()
                            result.add(tuple(flist))
        return list(result)
