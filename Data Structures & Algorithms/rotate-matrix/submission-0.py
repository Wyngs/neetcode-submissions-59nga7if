class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            temp = matrix[-i-1]
            matrix[-i-1] = matrix[i]
            matrix[i] = temp
        counter = 1
        for i in range(n-1):
            for j in  range(counter,n):
                temp  = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
            counter +=1


