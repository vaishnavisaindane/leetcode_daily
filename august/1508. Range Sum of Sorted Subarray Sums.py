class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result_arr=[]
        for i in range(n):
            current_sum=0
            for j in range(i,n):
                current_sum += nums[j]
                result_arr.append(current_sum)
        result_arr.sort()
        return sum(result_arr[(left-1):right]) % int((10**9)+7)
