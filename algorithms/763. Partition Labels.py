class Solution:
    def partitionLabels(self, S: 'str') -> 'List[int]':
        last = {c: i for i, c in enumerate(S)}
        
        # This stores the partitions. Each partition has 2 components: start index and end index
        result = [ [0, last[S[0]]] ]

        for ch_curr_i, c in enumerate(S):
            if ch_curr_i == 0:
                continue

            partition_start, partition_end = result[-1]
            ch_last_i = last[c]

            if ch_last_i <= partition_end:
                continue
            

            if ch_curr_i > partition_end and ch_last_i > partition_end:
                result.append([ch_curr_i, ch_last_i])
                

            if partition_start <= ch_curr_i <= partition_end and ch_last_i > partition_end:
                result[-1][1] = ch_last_i

        return [r[1]-r[0]+1 for r in result]
