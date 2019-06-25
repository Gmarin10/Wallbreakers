class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        B = A[:][:]
        #B is the matrix that will hold the transpose of A
        for x in range(len(A)):
            for y in range(len(A[0])):
                B[x][y] = A[y][x]       # not proper solution
        return (B)
