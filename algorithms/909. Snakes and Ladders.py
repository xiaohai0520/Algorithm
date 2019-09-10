class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        q = collections.deque([(1, 0)])
        visited = set([1])
        while q: 
            for i in range(len(q)):
                square, turn = q.popleft()
                for i in range(square + 1, square + 7):
                    row, col = (i - 1)//n, (i - 1) % n 

                    chute = board[n - row - 1][col if row % 2 == 0 else n - col - 1]
                    if chute > 0: i = chute 
                    if i == n*n: return turn + 1
                    if i not in visited:
                        visited.add(i)
                        q.append((i, turn + 1))
        return -1 
