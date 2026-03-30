class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = (len(board[0]))

        def backtrack(index, row, col):

            if index == len(word):
                return True
            
            if row >= rows or row < 0 or col < 0 or col >= cols:
                return False
            
            if board[row][col] != word[index]:
                return False
            
            temp = board[row][col]
            board[row][col] = ""

            found = (
                backtrack(index+1, row-1 ,col) or 
                backtrack(index+1, row ,col-1) or
                backtrack(index+1, row ,col+1) or
                backtrack(index+1, row+1 ,col)
            )

            board[row][col] = temp
            return found
                          

        for i in range(rows):
            for j in range(cols):
                if backtrack(0,i,j):
                    return True

        return False
        
        