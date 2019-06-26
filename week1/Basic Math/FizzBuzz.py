class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        #List A will contain the fizzbuzz output
        A= []
        
        #start range at 1, since default would start at 0, n+1 to include numbern in the range
        for num in range(1,n+1):
            
            #checks if num is divisible by both 5 and 3
            if (num%5==0 and num%3==0):
                A.append("FizzBuzz")
                
            #checks if num is divisible by 5
            elif (num%5==0):
                A.append("Buzz")
            
            #checks if num is divisible by 3
            elif (num%3==0):
                A.append("Fizz")
            #if num is not divisible by either 5 or 3 it gets added as a string
            else:
                A.append(str(num))
                
        return A
