二分搜索，关键是判断哪边是排序的
先取左右边界的中间值 做判断，看是否等于target
在不等于target的情况下，判断左边是否是排序的，如果是，看target是否在左边的范围里，如果在，则将右边界左移，否则，左边界右移
如果左边不是排序的，那右边一定是排序的，做同样的操作即可。


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l,r = 0,len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    
