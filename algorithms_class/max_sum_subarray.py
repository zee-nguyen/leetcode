# Find the max sum over all subarrays of given array of integer
import itertools

class MaxSumSubarrays:
    def brute_force(self, A) -> int:
        mx = float("-inf")
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                total = 0
                for k in range(i, j+1):
                    total += A[k]
                mx = max(total, mx)
        return mx

    # def dp(self, A) -> int:
    #     min_sum = max_sum = 0
    #     for running_sum in itertools.accumulate(A):
    #         min_sum = min(min_sum, running_sum)
    #         max_sum = max(max_sum, running_sum - min_sum)
    #     return max_sum


test = MaxSumSubarrays()
A = [904, 40, 523, 12, -335, -385, -124, 481, -31]
print(test.brute_force(A))