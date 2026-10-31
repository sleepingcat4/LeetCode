class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat # we inspect matrix 
        result = [[0] * c for _ in range(r)]
        for i in range(m):
            for j in range(n):
                k = n * i + j
                new_row = k // c 
                new_col = k % c 
                result[new_row][new_col] = mat[i][j]
        return result 
