class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i,j,length):
            if length == len(word)-1:
                if board[i][j] == word[-1]:
                    return True
            # If this character is incorrect return
            if board[i][j] != word[length]:
                return
            # remove the current letter on the board
            # so dfs doensn't hit it twice
            cur_letter = board[i][j]
            board[i][j] = '#'
            # if you can move right, move right
            if j < len(board[0]) -1:
                if dfs(i,j+1,length+1):
                    return True
            if j > 0:
                if dfs(i,j-1,length+1):
                    return True
            if i < len(board) - 1:
                if dfs(i + 1, j, length+1):
                    return True
            if i > 0:
                if dfs(i -1, j, length+1):
                    return True
            board[i][j] = cur_letter
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True

        return False