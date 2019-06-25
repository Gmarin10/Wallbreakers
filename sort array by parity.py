class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        #initializing arrays to hold even, odd and combined lists
        even = []
        odd = []
        eventhenodd = []
        
        # one loop that adds number to appropriate list for even or odd number
        for num in A:
            if (num%2) == 0:
                even.append(num)
            else:
                odd.append(num)
        #combines then returns both lists in proper order of even then odd
        eventhenodd = even + odd
        return (eventhenodd)
