from typing import List


class Solution:
    island_count = 0
    is_island = False
    tracker={}

    def DFS(self, i, j, grid):
        if i > len(grid)-1 or i < 0 or j > len(grid[0])-1 or j < 0:
            return
        if grid[i][j] in ('0', '2'):
            return
        if grid[i][j] == '1':
            self.is_island = True
            grid[i][j] = '2'
            self.DFS(i-1, j, grid)
            self.DFS(i+1, j, grid)
            self.DFS(i, j-1, grid)
            self.DFS(i, j+1, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.is_island = False
                    self.DFS(i, j, grid)
                    if self.is_island:
                        self.island_count += 1
        return self.island_count


if __name__ == "__main__":
    
    
    t = Solution().numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
    )
    print(t)
    
    
    t = Solution().numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
    )
    print(t)
