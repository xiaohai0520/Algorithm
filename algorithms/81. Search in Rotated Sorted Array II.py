class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        l,r = 0,len(nums)-1
        while l <= r:
            while l < r and nums[l] == nums[r]:
                l += 1
            mid = l + (r-l) //2
            if nums[mid] == target:
                return True
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
