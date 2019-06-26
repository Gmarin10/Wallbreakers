class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        A = []
        
        #combines list into 1 number as a string
        n = ''.join(map(str,digits))
        
        #new varable that adds 1 to string
        num = int(n)+1
        
        #counter for index
        n = 0
        
        #goes 1 by 1 through num to see each digit
        for digit in str(num):
            
            #adds digits to A as an int
            A.append(int(digit))
            n=n+1
        
        #initial idea to just find last digit and add 1 to it
        #digits[len(digits)-1] = digits[len(digits)-1]+1
        
        
        return A
