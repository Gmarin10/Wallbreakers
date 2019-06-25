class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        B = A[:][:]
        d = len(A[0])
        for x in range(len(A)):
            for y in range(len(A[0])):
                
                #flips bit horizontally
                #B[x][~y] = A[x][y]^1   #does not flip properly
                
                #inverts bits
                B[x][y] = A [x][y]^1
                
        return B            
        
