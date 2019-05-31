class Solution:
    # recursive solution
    def fib(self, N: int) -> int:
        if (N == 0 or N == 1):
            return N
        else:
            return fib(N-1) + fib(N-2)

    # array solution
    def fibArr(self, N: int) -> int:
        if (N == 0 or N == 1):
            return N
        
        arr = [0] * (N + 1)
        arr[0] = 0
        arr[1] = 1
        for i in range(2, len(arr)):
            arr[i] = arr[i-1] + arr[i-2]
            
        return arr[N]


obj = Solution()
print(obj.fibArr(2))