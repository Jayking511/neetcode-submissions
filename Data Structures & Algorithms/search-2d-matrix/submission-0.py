class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix)-1
        row = -1
        while top <= bot:
            row = (top+bot) // 2
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bot = row-1
            else:
                break
        left, right = 0, len(matrix[row])-1
        while left <= right:
            middle_index = (left+right)//2
            if matrix[row][middle_index] == target:
                return True
            elif matrix[row][middle_index] > target:
                right = middle_index - 1
            else:
                left = middle_index + 1
        return False