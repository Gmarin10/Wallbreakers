class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        # A is the list that will contain self dividing numbers
        A= []
        
        #checks to see if number is divisible by all of its digits
        #if any number is 0 or indevisible by its digit it will imediatly return false
        def isselfdiv(num): 
            for digit in str(num):
                if (digit == '0' or num%int(digit) != 0):
                    return False
            return True
        
        #call isselfdiv() for each number in the range left to right, given left <= right
        for num in range(left, right + 1):
            if isselfdiv(num):
                A.append(num)
        
        
        return A
