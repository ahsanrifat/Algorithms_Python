from typing import List


class Solution:
    def index_to_matrix_value(self, index, matrix):
        col_count = len(matrix[0])
        row = int(index/col_count)
        col = int(index % col_count)
        return matrix[row][col]

    def binary_search(self, start_index, end_index, matrix, target):
        if end_index < start_index:
            return False
        mid_index = (end_index+start_index)//2
        if self.index_to_matrix_value(start_index, matrix) == target:
            return True
        if self.index_to_matrix_value(end_index, matrix) == target:
            return True
        mid_val = self.index_to_matrix_value(mid_index, matrix)
        if mid_val == target:
            return True
        elif mid_val < target:
            return self.binary_search(mid_index+1, end_index, matrix, target)
        else:
            return self.binary_search(start_index, mid_index-1, matrix, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col_count = len(matrix[0])
        row_count = len(matrix)
        start_index = 0
        last_index = col_count*row_count-1
        return self.binary_search(start_index, last_index, matrix, target)


if __name__ == "__main__":
    print(Solution().searchMatrix(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 7))
