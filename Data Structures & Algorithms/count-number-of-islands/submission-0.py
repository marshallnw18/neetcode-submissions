class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        rows, columns = len(grid), len(grid[0])

        def dfs(r,c):
            # establish base case
            if r < 0 or c < 0 or c >= columns or r >= rows or grid[r][c] == '0':
                return
            # mark cell as visited
            grid[r][c] = '0'
            
            # traverse rows and columns
            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)

        # logic for initiating a dfs 
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1':
                    dfs(r,c)
                    islands += 1
            
        return islands