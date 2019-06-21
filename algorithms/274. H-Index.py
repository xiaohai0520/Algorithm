class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)

        h_index = 0
        for i, num_cit_for_paper in enumerate(citations):
            if num_cit_for_paper >= i+1:
                h_index = i+1
            else:
                break
        return h_index
