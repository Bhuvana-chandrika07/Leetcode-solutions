class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board:
            return  

        self.rows = len(board)
        self.cols = len(board[0]) 

        for c in range(self.cols):
    
            if board[0][c] == 'O':
                self.dfs_save(board, 0, c)
 
            if board[self.rows - 1][c] == 'O':
                self.dfs_save(board, self.rows - 1, c)

        for r in range(self.rows):

            if board[r][0] == 'O':
                self.dfs_save(board, r, 0)
       
            if board[r][self.cols - 1] == 'O':
                self.dfs_save(board, r, self.cols - 1)

        for r in range(self.rows):
            for c in range(self.cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  
                elif board[r][c] == 'S':
                    board[r][c] = 'O'  

    def dfs_save(self, board, r, c):
    
        if (r < 0 or r >= self.rows or
            c < 0 or c >= self.cols or
            board[r][c] != 'O'):
            return

        board[r][c] = 'S'

        self.dfs_save(board, r + 1, c) # Sotto
        self.dfs_save(board, r - 1, c) # Sopra
        self.dfs_save(board, r, c + 1) # Destra
        self.dfs_save(board, r, c - 1) # Sinistra