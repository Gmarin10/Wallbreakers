class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        B = []
        #B is the matrix that will hold the transpose of A
        for x in A:
            for y in A[0]:
                B[x][y] = A[y][x] #should write to new matrix in B, returns error
        return (B)
