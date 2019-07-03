class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def gen_range(start, end):
            if start == end:
                return str(start)
            else:
                return "{0}->{1}".format(start, end)

        if not nums:
            return [gen_range(lower, upper)]

        start = lower
        missing_ranges = []
        for num in nums:
            if start < num:
                missing_ranges.append(gen_range(start, num - 1))

            start = num + 1

        if nums[-1] != upper:
            missing_ranges.append(gen_range(start, upper))

        return missing_ranges
        
